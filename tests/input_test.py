from StreamShield.input import process_input

from playsound import playsound

import cv2


path = r"D:\YOLO Fine Tuning\Data\input\2025-02-25 10-23-40.mkv"

process_data = process_input(path)

# playsound(process_data['audio'])

if "frames" in process_data and hasattr(process_data["frames"], "__iter__"):
  for frame in process_data["frames"]:

    # display video frame-by-frame
    cv2.imshow("Output", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
