"""
input_handler.py

This module handles various input sources (images, videos, audio, and webcam streams)
and integrates with the configuration manager to decide on processing steps.
For example, audio extraction is only performed if the configuration has a valid
beep words file path.
"""

import os
from StreamShield.config import ConfigManager
from .audio_extractor import extract_audio
from .frame_extractor import frame_generator
from .webcam_stream import start_webcam_stream

# Initialize a global ConfigManager instance.
config_manager = ConfigManager()


def process_input(input_source):
    """
    Processes the given input source based on its type (image, video, audio, or webcam)
    while considering configuration parameters from the ConfigManager.

    Parameters:
        input_source (str): Path to a file or the string "webcam" for live streaming.

    Returns:
        dict: A dictionary containing processed data, e.g., {"frames": [...], "audio": ...}.
    """
    data = {}

    # Load current configuration.
    config = config_manager.get_config()
    beep_words_file = config.get("beep_words", "")

    # If a VideoCapture object is passed, assume it's a live stream.
    import cv2
    if isinstance(input_source, cv2.VideoCapture):
        data["frames"] = start_webcam_stream(video_capture=input_source)
    elif isinstance(input_source, str) and input_source == "webcam":
        data["frames"] = start_webcam_stream()

    # Process file-based input.
    elif os.path.exists(input_source):
        ext = os.path.splitext(input_source)[1].lower()
        # If the input is an image, simply return the file as a frame.
        if ext in [".jpg", ".jpeg", ".png"]:
            data["frames"] = [input_source]
        # If the input is a video file, use a generator to yield frames one at a time.
        elif ext in [".mp4", ".avi", ".mov", ".mkv"]:
            data["frames"] = frame_generator(input_source)
            # Only extract audio if the configuration has a valid beep words file.
            if beep_words_file and os.path.exists(beep_words_file):
                data["audio"] = extract_audio(input_source)
        # If the input is an audio file, assign the file path directly.
        elif ext in [".mp3", ".wav"]:
            data["audio"] = input_source
        else:
            raise ValueError("Unsupported file type.")
    else:
        raise ValueError("Input source not found or invalid.")

    return data


# if __name__ == "__main__":
#     # Example usage: Processing a sample video file.
#     sample_video = r"D:\YOLO Fine Tuning\Data\input\2025-02-25 10-23-40.mkv"
#     processed_data = process_input(sample_video)
#     print("Processed data:", processed_data)
