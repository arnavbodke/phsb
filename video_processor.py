import cv2
from detector import detect_objects


def process_video(input_path, output_path):

    cap = cv2.VideoCapture(input_path)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    out = cv2.VideoWriter(
        output_path,
        fourcc,
        fps,
        (width, height)
    )

    while cap.isOpened():

        ret, frame = cap.read()

        if not ret:
            break

        detections = detect_objects(frame)

        for detection in detections:

            x1, y1, x2, y2 = detection["box"]

            label = detection["label"]

            confidence = detection["confidence"]

            text = f"{label} {confidence:.2f}"

            # Bounding Box
            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            # Text
            cv2.putText(
                frame,
                text,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

        out.write(frame)

    cap.release()
    out.release()