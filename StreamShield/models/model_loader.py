"""
model_loader.py

This module loads and manages AI models for the sensitive_blur package.
It supports:
- YOLO (for video frame object detection)
- VOSK (for speech-to-text processing)

It ensures optimized loading and execution of both models, allowing parallel
processing of video frames and audio.
"""

import torch
import vosk
import threading
from ultralytics import YOLO


class ModelLoader:
    def __init__(self, device="cuda" if torch.cuda.is_available() else "cpu"):
        """
        Initializes the model loader and loads YOLO and VOSK models.

        Parameters:
            device (str): "cuda" for GPU or "cpu" for CPU processing.
        """
        self.device = device
        self.yolo_model = None
        self.vosk_model = None

    def load_yolo(self, model_path="yolov5s.pt"):
        """
        Loads the YOLO model for object detection.

        Parameters:
            model_path (str): Path to the YOLO model weights.

        Returns:
            The loaded YOLO model.
        """
        print("[INFO] Loading YOLO model...")
        self.yolo_model = YOLO(model_path)
        print("[INFO] YOLO model loaded successfully.")
        return self.yolo_model

    def load_vosk(self, model_path="model"):
        """
        Loads the VOSK model for speech-to-text processing.

        Parameters:
            model_path (str): Path to the VOSK model directory.

        Returns:
            The loaded VOSK model.
        """
        print("[INFO] Loading VOSK model...")
        self.vosk_model = vosk.Model(model_path)
        print("[INFO] VOSK model loaded successfully.")
        return self.vosk_model

    def load_models(self, yolo_path="yolov5s.pt", vosk_path="model"):
        """
        Loads both YOLO and VOSK models in parallel using threading.

        Parameters:
            yolo_path (str): Path to the YOLO model weights.
            vosk_path (str): Path to the VOSK model directory.

        Returns:
            dict: A dictionary containing both loaded models.
        """
        threads = []

        # Thread for YOLO
        yolo_thread = threading.Thread(target=self.load_yolo, args=(yolo_path,))
        threads.append(yolo_thread)

        # Thread for VOSK
        vosk_thread = threading.Thread(target=self.load_vosk, args=(vosk_path,))
        threads.append(vosk_thread)

        # Start threads
        for thread in threads:
            thread.start()

        # Wait for both threads to finish
        for thread in threads:
            thread.join()

        print("[INFO] Both models loaded successfully.")
        return {"yolo": self.yolo_model, "vosk": self.vosk_model}
