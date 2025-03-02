from StreamShield.models import ModelLoader

loader = ModelLoader()

yolo_path = r"D:\YOLO Fine Tuning\runs\detect\train3\weights\best.pt"
loader.load_yolo(yolo_path)
model = loader.yolo_model
# print(model)

vosk_path = r"C:\Users\ask50\Desktop\Privacy Lens\Privacy Lens\server\StreamShield\vosk-model-small-en-in-0.4"
loader.load_vosk(vosk_path)
model = loader.vosk_model