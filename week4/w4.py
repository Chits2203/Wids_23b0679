import cv2
import numpy as np
import mediapipe as mp

# -------------------------------
# Simple background removal
# (removes white / near-uniform background)
# -------------------------------
def remove_background(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Threshold for white / light background
    _, mask = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)

    result = cv2.bitwise_and(img, img, mask=mask)
    return result, mask


# -------------------------------
# Overlay helper
# -------------------------------
def overlay_image(frame, overlay, mask, x, y, w, h):
    overlay_resized = cv2.resize(overlay, (w, h))
    mask_resized = cv2.resize(mask, (w, h))

    roi = frame[y:y+h, x:x+w]
    if roi.shape[0] != h or roi.shape[1] != w:
        return frame

    mask_inv = cv2.bitwise_not(mask_resized)

    bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
    fg = cv2.bitwise_and(overlay_resized, overlay_resized, mask=mask_resized)

    frame[y:y+h, x:x+w] = cv2.add(bg, fg)
    return frame


# -------------------------------
# Load overlay image
# -------------------------------
overlay_path = input("Enter path to overlay image: ")
overlay_img = cv2.imread(overlay_path)

if overlay_img is None:
    raise IOError("Overlay image not found")

overlay_img, overlay_mask = remove_background(overlay_img)

# -------------------------------
# MediaPipe Face Mesh
# -------------------------------
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1)

# Landmark indices for regions
LANDMARKS = {
    "nose": [1],
    "forehead": [10],
    "chin": [152],
    "head": [10],
    "mouth": [13],
    "eyes": [33, 263],
    "both_cheeks": [234, 454]
}

# Default placement
placement = "nose"

# -------------------------------
# Webcam
# -------------------------------
cap = cv2.VideoCapture(0)

print("""
Controls:
1 - Head
2 - Forehead
3 - Eyes
4 - Nose (default)
5 - Mouth
6 - Chin
7 - Both Cheeks
q - Quit
""")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = face_mesh.process(rgb)

    if result.multi_face_landmarks:
        face = result.multi_face_landmarks[0].landmark

        if placement in LANDMARKS:
            points = LANDMARKS[placement]
            xs = [int(face[p].x * w) for p in points]
            ys = [int(face[p].y * h) for p in points]

            cx, cy = int(np.mean(xs)), int(np.mean(ys))

            # Dynamic sizing based on placement
            if placement == "nose":
                ow, oh = int(w * 0.08), int(h * 0.08)
            elif placement in ["eyes", "mouth"]:
                ow, oh = int(w * 0.18), int(h * 0.12)
            elif placement == "forehead":
                ow, oh = int(w * 0.25), int(h * 0.15)
            elif placement == "chin":
                ow, oh = int(w * 0.15), int(h * 0.12)
            elif placement == "both_cheeks":
                ow, oh = int(w * 0.35), int(h * 0.15)
            else:  # head
                ow, oh = int(w * 0.35), int(h * 0.30)

            x = max(cx - ow // 2, 0)
            y = max(cy - oh // 2, 0)

            frame = overlay_image(
                frame, overlay_img, overlay_mask, x, y, ow, oh
            )

    cv2.imshow("AR Overlay System", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('1'):
        placement = "head"
    elif key == ord('2'):
        placement = "forehead"
    elif key == ord('3'):
        placement = "eyes"
    elif key == ord('4'):
        placement = "nose"
    elif key == ord('5'):
        placement = "mouth"
    elif key == ord('6'):
        placement = "chin"
    elif key == ord('7'):
        placement = "both_cheeks"

cap.release()
cv2.destroyAllWindows()
