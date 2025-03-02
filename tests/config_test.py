from StreamShield.config import ConfigManager

config = ConfigManager()

hide_elements = ["login_forms", "face"]

path = "test.txt"

config.update_config(hide_elements=hide_elements, beep_words_file_path=path)

print("Hide Elements:", config.get_hide_elements())
print("Beep words:", config.get_beep_words())

print("Configuration:", config.get_config())

