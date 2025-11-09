import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Camera not detected. Try index 1 or check drivers.")
else:
    ret, frame = cap.read()
    if ret:
        print("Camera OK. Frame shape:", frame.shape)
        cv2.imshow("Test", frame)
        cv2.waitKey(1000)  # shows frame for 1 second
        cv2.destroyAllWindows()
    else:
        print("Camera opened but couldn't read frame.")
cap.release()
