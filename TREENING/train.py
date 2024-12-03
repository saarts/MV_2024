from ultralytics import YOLO

# Saab teada kasutade jada
import os
print(os.getcwd())

# Mudel, mida aluseks kasutada
model = YOLO("yolo11n.pt")

# Treenime
results = model.train(data="datasets/data.yaml", epochs = 50, imgsz=640)