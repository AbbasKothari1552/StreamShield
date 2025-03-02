"""
config_manager.py

This module manages configuration settings for the sensitive_blur package.
It provides an interface to update configuration parameters via API calls.
Parameters include:
    - hide_elements: A dictionary indicating which UI elements to hide.
    - beep_words: A file path to a text file containing beep words.

Users can update these parameters dynamically (for example, when a website API
passes a dropdown selection for hide_elements and a file path for custom beep_words).
"""

import os

# Default configuration values
DEFAULT_CONFIG = {
    "hide_elements": {
        "login_forms": True,   # Default: hide login forms
        "links": True          # Default: hide links
    },
    "beep_words": "default_beep_words.txt"  # Default file path for beep words
}


class ConfigManager:
    def __init__(self):
        """
        Initialize the configuration manager with default settings.
        """
        # Make a copy of the default configuration
        self.config = DEFAULT_CONFIG.copy()

    def update_config(self, hide_elements=None, beep_words_file_path=None):
        """
        Update configuration parameters based on API inputs.

        Parameters:
            hide_elements (str or list of str, optional):
                The UI elements to hide. This can be a single string (e.g., "login_forms")
                or a list of strings (e.g., ["login_forms", "links"]). Only the available
                options ["login_forms", "links"] will be used.

            beep_words_file_path (str, optional):
                A file path pointing to a text file that contains custom beep words.
        """
        if hide_elements is not None:
            # Normalize hide_elements to a list if a single string is passed.
            if isinstance(hide_elements, str):
                hide_elements = [hide_elements]

            # Define the allowed options.
            available_options = ["login_forms", "links"]
            # Create a dictionary setting True for selected options, False otherwise.
            updated_hide_elements = {
                option: (option in hide_elements) for option in available_options
            }
            self.config["hide_elements"] = updated_hide_elements

        if beep_words_file_path is not None:
            # Verify that the provided file path exists.
            if os.path.exists(beep_words_file_path):
                self.config["beep_words"] = beep_words_file_path
            else:
                # Optionally, you might raise an exception or log an error here.
                print(f"Warning: The file '{beep_words_file_path}' does not exist. Using the existing configuration.")

    def get_hide_elements(self):
        """
        Return the current configuration for hide_elements.

        Returns:
            dict: Configuration dictionary for UI elements to hide.
        """
        return self.config.get("hide_elements", {})

    def get_beep_words(self):
        """
        Read the beep words file (provided as a file path) and return a list of beep words.
        If the file cannot be read, returns an empty list.

        Returns:
            list: List of beep words.
        """
        file_path = self.config.get("beep_words", "")
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r') as f:
                    # Each beep word is assumed to be on a separate line.
                    beep_words = [line.strip() for line in f if line.strip()]
                return beep_words
            except Exception as e:
                # Optionally log the error here.
                print(f"Error reading beep words file: {e}")
        else:
            print(f"Beep words file '{file_path}' not found.")
        return []

    def get_config(self):
        """
        Return the complete current configuration dictionary.

        Returns:
            dict: The entire configuration.
        """
        return self.config
