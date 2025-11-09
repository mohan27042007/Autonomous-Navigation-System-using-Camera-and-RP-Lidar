"""
Adds real-time obstacle proximity alerts and simple navigation hints
on top of the camera + LiDAR fusion system.
"""

from ultralytics import YOLO
from rplidar import RPLidar
import cv2
import threading
import numpy as np
import time
import winsound   # Windows beep; comment out if using Linux

PORT = 'COM3'
MODEL_PATH = 'models/yolov8n.pt'

latest_distance = {"Left": 0, "Center": 0, "Right": 0}
stop_threads = False
ALERT_THRESHOLD = 1000   # distance in cm to trigger alert (~10 m)

# ---------------------- LiDAR Thread ----------------------
def lidar_thread():
    global latest_distance, stop_threads
    try:
        lidar = RPLidar(PORT)
        lidar.start_motor()
        time.sleep(1)
        print("LIDAR started (alert mode).")

        for scan in lidar.iter_scans():
            if stop_threads:
                break
            left, center, right = [], [], []

            for (_, angle, dist) in scan:
                if 0 <= angle < 60 or angle > 300:
                    right.append(dist)
                elif 60 <= angle < 120:
                    center.append(dist)
                elif 120 <= angle < 180:
                    left.append(dist)

            latest_distance["Left"] = np.mean(left) if left else 0
            latest_distance["Center"] = np.mean(center) if center else 0
            latest_distance["Right"] = np.mean(right) if right else 0

        lidar.stop()
        lidar.stop_motor()
        lidar.disconnect()

    except Exception as e:
        print("LIDAR thread error:", e)


# ---------------------- Decision Logic ----------------------
def navigation_decision():
    """Returns navigation hint and color based on distances."""
    L, C, R = latest_distance["Left"], latest_distance["Center"], latest_distance["Right"]

    if C and C < ALERT_THRESHOLD:
        hint = "STOP - Obstacle Ahead"
        color = (0, 0, 255)  # red
        winsound.Beep(900, 150)
    elif L and L < ALERT_THRESHOLD:
        hint = "Turn Right"
        color = (0, 165, 255)  # orange
        winsound.Beep(700, 150)
    elif R and R < ALERT_THRESHOLD:
        hint = "Turn Left"
        color = (0, 165, 255)
        winsound.Beep(700, 150)
    else:
        hint = "Path Clear"
        color = (0, 255, 0)    # green
    return hint, color


# ---------------------- Main Loop ----------------------
def main():
    global stop_threads
    lidar_t = threading.Thread(target=lidar_thread)
    lidar_t.start()

    model = YOLO(MODEL_PATH)
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    print("Alert system running... Press ESC to exit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)
        annotated = results[0].plot()

        # Draw sector boundaries
        width = frame.shape[1]
        h = frame.shape[0]
        third = width // 3
        cv2.line(annotated, (third, 0), (third, h), (255, 255, 255), 1)
        cv2.line(annotated, (2 * third, 0), (2 * third, h), (255, 255, 255), 1)

        # Get  decision + overlay
        hint, color = navigation_decision()
        cv2.putText(annotated, f"L:{latest_distance['Left']:.0f}  "
                               f"C:{latest_distance['Center']:.0f}  "
                               f"R:{latest_distance['Right']:.0f}",
                    (20, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
        cv2.putText(annotated, hint, (20, 70),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

        cv2.imshow("Obstacle Alert System", annotated)
        if cv2.waitKey(1) & 0xFF == 27:
            stop_threads = True
            break

    cap.release()
    cv2.destroyAllWindows()
    stop_threads = True
    lidar_t.join()
    print("Alert system stopped cleanly.")

if __name__ == "__main__":
    main()


