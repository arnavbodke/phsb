from ultralytics import YOLO
import cv2

# Load trained model
model = YOLO("best.pt")

# Class names
CLASS_NAMES = {
    0: "Pothole",
    1: "Speedbreaker"
}


def detect_objects(frame):

    results = model(frame)

    detections = []

    for result in results:

        boxes = result.boxes

        for box in boxes:

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            confidence = float(box.conf[0])

            class_id = int(box.cls[0])

            label = CLASS_NAMES.get(class_id, "Unknown")

            detections.append({
                "box": (x1, y1, x2, y2),
                "confidence": confidence,
                "label": label
            })

    return detections