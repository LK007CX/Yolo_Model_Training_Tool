import cv2

cap = cv2.VideoCapture('rtsp://192.168.0.2:8554/test')
while cap.isOpened():
    (status, frame) = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()