from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def detect_objects(frame):
    results = model(frame)
    detections = []
    for box in results[0].boxes:
        cls_id = model.names[int(box.cls)]
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        detections.append((cls_id, x1, y1, x2, y2))
    return detections