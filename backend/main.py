import cv2
from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolov8n.pt")

# Load video
cap = cv2.VideoCapture("traffic.mp4")

# Define queue region (adjust later if needed)
ROI_START = 300
ROI_END = 600

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # YOLO detection
    results = model(frame, classes=[2, 3, 5, 7])

    queue_count = 0

    # Loop through detected vehicles
    for box in results[0].boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])

        # Calculate center of vehicle
        center_y = (y1 + y2) // 2

        # Check if vehicle is inside queue area
        if ROI_START < center_y < ROI_END:
            queue_count += 1

    # Draw queue region
    cv2.rectangle(
        frame,
        (0, ROI_START),
        (frame.shape[1], ROI_END),
        (255, 255, 0),
        2
    )

    # Display queue count
    cv2.putText(
        frame,
        f"Queue Length: {queue_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("Queue Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
