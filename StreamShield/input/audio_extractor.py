# audio_extractor.py

import subprocess

def extract_audio(video_path, output_audio_path="extracted_audio.wav"):
    """
    Extract audio from a video file using FFmpeg.

    Parameters:
        video_path (str): Path to the video file.
        output_audio_path (str): Path where the extracted audio will be saved.

    Returns:
        str: The file path to the extracted audio.
    """
    # Ensure FFmpeg is installed and in your PATH.
    command = [
        "ffmpeg",
        "-i", video_path,
        "-q:a", "0",
        "-map", "a",
        output_audio_path,
        "-y"  # Overwrite output file without asking
    ]
    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return output_audio_path
