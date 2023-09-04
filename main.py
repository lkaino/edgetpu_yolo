from ultralytics import YOLO
model_name = 'yolov8s'
input_width = 320
input_height = 320
model = YOLO(f"{model_name}.pt")
model.export(format="edgetpu", imgsz=[input_height,input_width], int8=True)