from ultralytics import YOLO


model = YOLO('yolov8n.pt')


# Training.
results = model.train(
   data=r'C:\Users\Farhang\Desktop\yolov8_projects\human\Human-Detection-3\data.yaml',
   imgsz=640,
   epochs=20,
   batch=8,
   save=True,
   device = 0,
   pretrained = True,
   name='yolov8n_custom')