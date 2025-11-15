from ultralytics import YOLO
import cv2
import time

# Load model
model = YOLO("models/yolov8n.pt")   # use nano model for speed

# Open webcam (index 0)
cap = cv2.VideoCapture(1)
if not cap.isOpened():
    raise IOError("Cannot open webcam")

# reduce resolution for speed
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    start = time.time()
    results = model(frame, classes=[0, 1, 2, 3, 5, 7], verbose = False)    # inference
    annotated = results[0].plot()         # draw boxes
    end = time.time()

    fps = 1 / (end - start)
    cv2.putText(annotated, f"FPS: {fps:.2f}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.imshow("YOLOv8 Camera Detection", annotated)

    if cv2.waitKey(1) & 0xFF == 27:      # ESC to quit
        break

cap.release()
cv2.destroyAllWindows()
