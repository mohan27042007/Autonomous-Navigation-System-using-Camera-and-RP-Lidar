# This file is an optimized version of fusion.py.
# This is the final py program which we run to get the output.

# Both fusion.py and optimize.py gives same results.
# However, optimize.py has better performance, logging and configuration options.
"""
Final optimized version of the Autonomous Navigation System
with configuration, logging, and performance improvements.
"""

from ultralytics import YOLO
from rplidar import RPLidar
import cv2, threading, numpy as np, time, json, os, csv

CONFIG_PATH = "config/settings.json"

# ------------------- Load Config -------------------
with open(CONFIG_PATH, "r") as cfg:
    CONFIG = json.load(cfg)

PORT = CONFIG["PORT"]
MODEL_PATH = CONFIG["MODEL_PATH"]
ALERT_THRESHOLD = CONFIG["ALERT_THRESHOLD"]
FRAME_W, FRAME_H = CONFIG["FRAME_WIDTH"], CONFIG["FRAME_HEIGHT"]
LOG_ENABLED = CONFIG["LOG_ENABLED"]
LOG_PATH = CONFIG["LOG_PATH"]

latest_distance = {"Left": 0, "Center": 0, "Right": 0}
stop_threads = False
frame_counter, start_time = 0, time.time()

# ------------------- LiDAR Thread -------------------
def lidar_thread():
    global latest_distance, stop_threads
    lidar = RPLidar(PORT)
    lidar.start_motor()
    time.sleep(1)
    print("[LIDAR] Running...")

    for scan in lidar.iter_scans():
        if stop_threads: break
        left, center, right = [], [], []
        for (_, angle, dist) in scan:
            if 0 <= angle < 60 or angle > 300:
                right.append(dist)
            elif 60 <= angle < 120:
                center.append(dist)
            elif 120 <= angle < 180:
                left.append(dist)
        latest_distance = {
            "Left": np.mean(left) if left else 0,
            "Center": np.mean(center) if center else 0,
            "Right": np.mean(right) if right else 0
        }

    lidar.stop(); lidar.stop_motor(); lidar.disconnect()
    print("[LIDAR] Stopped.")

# ------------------- Logging -------------------
def log_data(distances):
    if not LOG_ENABLED: return
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    with open(LOG_PATH, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([time.time(), distances["Left"], distances["Center"], distances["Right"]])

# ------------------- Alert Decision -------------------
def navigation_hint(dist):
    L, C, R = dist["Left"], dist["Center"], dist["Right"]
    if C and C < ALERT_THRESHOLD:
        return "STOP - Obstacle Ahead", (0,0,255)
    elif L and L < ALERT_THRESHOLD:
        return "Turn Right", (0,165,255)
    elif R and R < ALERT_THRESHOLD:
        return "Turn Left", (0,165,255)
    return "Path Clear", (0,255,0)

# ------------------- Main -------------------
def main():
    global stop_threads, frame_counter, start_time
    lidar_t = threading.Thread(target=lidar_thread, daemon=True)
    lidar_t.start()

    model = YOLO(MODEL_PATH)
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_W)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_H)

    print("[SYSTEM] Running optimized navigation... Press ESC to exit.")
    while True:
        ret, frame = cap.read()
        if not ret: break
        frame_counter += 1

        # YOLO inference
        results = model(frame, verbose=False)
        annotated = results[0].plot()

        # sector lines
        width, h = frame.shape[1], frame.shape[0]
        one_third = width // 3
        cv2.line(annotated, (one_third, 0), (one_third, h), (200,200,200), 1)
        cv2.line(annotated, (2*one_third, 0), (2*one_third, h), (200,200,200), 1)

        # decision + display
        hint, color = navigation_hint(latest_distance)
        cv2.putText(annotated, f"L:{latest_distance['Left']:.0f} "
                               f"C:{latest_distance['Center']:.0f} "
                               f"R:{latest_distance['Right']:.0f}",
                    (20,35), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
        cv2.putText(annotated, hint, (20,70), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

        # FPS counter
        fps = frame_counter / (time.time() - start_time)
        cv2.putText(annotated, f"FPS: {fps:.1f}", (500,35),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)

        cv2.imshow("Optimized Navigation", annotated)
        log_data(latest_distance)

        if cv2.waitKey(1) & 0xFF == 27:
            stop_threads = True
            break

    cap.release(); cv2.destroyAllWindows()
    stop_threads = True
    lidar_t.join()
    print("[SYSTEM] Stopped cleanly.")

if __name__ == "__main__":
    main()
