from ultralytics import YOLO

# YOLO modelini yuklash
model_path = r"best.pt"

model = YOLO(model_path)

results = model.predict(source="test_img6.jpg",save=True,show=True)

# print(model.names)