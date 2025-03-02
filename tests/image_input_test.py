import cv2

from StreamShield.input import process_input

path = r"C:\Users\ask50\Videos\plastic\HdpeBottle1.jpeg"

data = process_input(path)

# Check if frames are present
if "frames" in data:
    for frame_path in data["frames"]:
        # Load the image using cv2.imread
        image = cv2.imread(frame_path)
        if image is not None:
            cv2.imshow("Output", image)
            # Wait for a key press to close the window.
            cv2.waitKey(0)
        else:
            print("Failed to load image from", frame_path)
cv2.destroyAllWindows()