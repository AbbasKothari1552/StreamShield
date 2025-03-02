import cv2

from StreamShield.input import process_input

cap = cv2.VideoCapture(0)
process_data = process_input(cap)

if "frames" in process_data:
    for frame in process_data["frames"]:
        cv2.imshow("Output", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cv2.destroyAllWindows()