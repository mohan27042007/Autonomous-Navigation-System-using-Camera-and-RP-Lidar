
"""
Code to Fuse The Camera (YOLOv8) object detection + RPLiDAR distance sensing.
"""

from ultralytics import YOLO
from rplidar import RPLidar, RPLidarException
import cv2
import threading
import numpy as np
import time

# ==========================
# USER SETTINGS
# ==========================
PORT = 'COM3'                     
MODEL_PATH = 'models/yolov8n.pt'  

# ==========================
# GLOBAL VARIABLES
# ==========================
latest_distance = {"Left": 0, "Center": 0, "Right": 0}
stop_threads = False


# ==========================
# LIDAR THREAD FUNCTION
# ==========================
def lidar_thread():
    """Reads data continuously from LiDAR and updates sector distances."""
    global latest_distance, stop_threads
    try:
        lidar = RPLidar(PORT)
        lidar.start_motor()
        time.sleep(1)
        print("LIDAR started successfully.")

        for scan in lidar.iter_scans():
            if stop_threads:
                break

            # divide space into 3 sectors (L, C, R)
            left_sector = []
            center_sector = []
            right_sector = []

            for (_, angle, dist) in scan:
                if 0 <= angle < 60 or angle > 300:
                    right_sector.append(dist)
                elif 60 <= angle < 120:
                    center_sector.append(dist)
                elif 120 <= angle < 180:
                    left_sector.append(dist)

            # Compute average distance for each sector
            latest_distance["Left"] = np.mean(left_sector) if left_sector else 0
            latest_distance["Center"] = np.mean(center_sector) if center_sector else 0
            latest_distance["Right"] = np.mean(right_sector) if right_sector else 0

        lidar.stop()
        lidar.stop_motor()
        lidar.disconnect()

    except RPLidarException as e:
        print("RPLidar error:", e)
    except Exception as e:
        print("General LiDAR error:", e)


# ==========================
# MAIN CAMERA + YOLO LOOP
# ==========================
def main():
    global stop_threads

    # start lidar in a separate thread
    lidar_t = threading.Thread(target=lidar_thread)
    lidar_t.start()

    # Load YOLOv8 model
    model = YOLO(MODEL_PATH)
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    print("Press ESC to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)
        annotated = results[0].plot()

        # Divide screen width into sectors (left/center/right)
        width = frame.shape[1]
        one_third = width // 3

        # draw vertical sector lines
        cv2.line(annotated, (one_third, 0), (one_third, frame.shape[0]), (255, 255, 255), 1)
        cv2.line(annotated, (2 * one_third, 0), (2 * one_third, frame.shape[0]), (255, 255, 255), 1)

        # overlay sector distances on top of each other
        cv2.putText(annotated, f"L: {latest_distance['Left']:.1f} cm", (30, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(annotated, f"C: {latest_distance['Center']:.1f} cm", (250, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(annotated, f"R: {latest_distance['Right']:.1f} cm", (470, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        cv2.imshow("Camera + LiDAR Fusion", annotated)
        key = cv2.waitKey(1)
        if key == 27:  # ESC key
            stop_threads = True
            break

    cap.release()
    cv2.destroyAllWindows()
    stop_threads = True
    lidar_t.join()
    print("Program exited cleanly.")


if __name__ == "__main__":
    main()
