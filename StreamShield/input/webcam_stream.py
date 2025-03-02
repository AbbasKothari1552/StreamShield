# webcam_stream.py

import cv2

def start_webcam_stream(video_capture=None):
    """
    Starts the webcam stream and returns frames in real-time.

    Returns:
        list: A list of frames captured (for demonstration, typically you'd stream continuously).
    """
    cap = video_capture if video_capture is not None else cv2.VideoCapture(0)

    while cap.isOpened():  # Capture 10 frames for example purposes
        ret, frame = cap.read()
        if not ret:
            break
        yield frame

    cap.release()
