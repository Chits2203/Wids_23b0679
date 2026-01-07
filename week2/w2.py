import cv2
import numpy as np
import mediapipe as mp

from mediapipe.tasks import python
from mediapipe.tasks.python import vision

video_path = "input_face_video.mp4"
overlay_path = "overlay.png"
model_path = "face_landmarker.task"
output_path = "output_video.mp4"

overlay_img = cv2.imread(overlay_path, cv2.IMREAD_UNCHANGED)

# Check if image loaded and ensure it has 4 channels
if overlay_img is None:
    raise ValueError(f"Could not load image at {overlay_path}")

if overlay_img.shape[2] == 3:
    print("Warning: overlay.png has no transparency. Converting to opaque (BGRA).")
    overlay_img = cv2.cvtColor(overlay_img, cv2.COLOR_BGR2BGRA)

BaseOptions = python.BaseOptions
FaceLandmarker = vision.FaceLandmarker
FaceLandmarkerOptions = vision.FaceLandmarkerOptions
VisionRunningMode = vision.RunningMode

options = FaceLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.VIDEO,
    num_faces=1
)

landmarker = FaceLandmarker.create_from_options(options)

cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(output_path, fourcc, fps, (w, h))

def overlay_transparent(frame, overlay, x, y, overlay_size=None):
    if overlay_size:
        overlay = cv2.resize(overlay, overlay_size)

    h_o, w_o, _ = overlay.shape
    if x + w_o > frame.shape[1] or y + h_o > frame.shape[0]:
        return frame

    alpha = overlay[:, :, 3] / 255.0
    for c in range(3):
        frame[y:y+h_o, x:x+w_o, c] = (1-alpha) * frame[y:y+h_o, x:x+w_o, c] + alpha * overlay[:, :, c]
    return frame


print("Processing video... press 'q' to quit display early")
timestamp = 0

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
    result = landmarker.detect_for_video(mp_image, timestamp)
    timestamp += int(1000 / fps)

    if result.face_landmarks:
        face = result.face_landmarks[0]
        
        lmk = face[10]
        fx, fy = int(lmk.x*w), int(lmk.y*h)

        
        overlay_size = (int(w*0.50), int(w*0.50))
        frame = overlay_transparent(frame, overlay_img, fx - overlay_size[0]//2, fy - overlay_size[1]//2, overlay_size)

    out.write(frame)
    cv2.imshow("Face Overlay NEW API", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Done! Saved to: {output_path}")
