# frame_extractor.py

import cv2

def frame_generator(video_path, frame_rate=1):
    """
    A generator function that yields frames from a video file.

    Parameters:
        video_path (str): Path to the video file.
        frame_rate (int): Process one frame per 'frame_rate' seconds.
                          Set to 1 to process every frame.

    Yields:
        frame (ndarray): The next video frame.
    """
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError(f"Unable to open video file: {video_path}")

    # Get the frames per second (FPS) of the video.
    fps = cap.get(cv2.CAP_PROP_FPS)
    # Calculate frame interval based on the desired frame_rate.
    # If frame_rate is 1, frame_interval becomes fps, meaning one frame per second.
    # To yield every frame, simply set frame_interval to 1.
    frame_interval = int(fps * frame_rate) if frame_rate > 0 else 1

    count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Yield frame if it matches the interval, or yield every frame if frame_interval is 1.
        # if frame_interval == 1 or count % frame_interval == 0:
        yield frame

        count += 1

    cap.release()
