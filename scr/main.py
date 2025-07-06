import cv2
from collections import defaultdict
from detection import detect_objects
from classification import classify_age_gender
from utils import resize_frame

video_path = "C:\\Users\\salma\\Downloads\\cur\\setraa.mp4"
cap = cv2.VideoCapture(video_path)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("output_demo.avi", fourcc, 20.0, (640, 480))

counts = defaultdict(int)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_resized = resize_frame(frame)
    detected_objects = detect_objects(frame_resized)

    for box in detected_objects:
        cls_id, x1, y1, x2, y2 = box
        cropped = frame_resized[y1:y2, x1:x2]

        if cls_id == "person":
            person_type = classify_age_gender(cropped)
            print("Classified:", person_type)  # Debug line
            counts[person_type] += 1
            color = (0, 255, 0)
            label_txt = person_type.replace("_", " ").title()
        else:
            counts[cls_id] += 1
            color = (255, 0, 0)
            label_txt = cls_id.title()

        cv2.rectangle(frame_resized, (x1, y1), (x2, y2), color, 2)
        cv2.putText(frame_resized, label_txt, (x1, y1 - 5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

    out.write(frame_resized)
    cv2.imshow("Detection", frame_resized)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print("\n🔢 Final Count Summary:")
for k, v in counts.items():
    print(f"{k.title()}: {v}")