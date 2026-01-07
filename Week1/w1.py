from PIL import Image
import cv2
import numpy as np

# 1. Load foreground image (Pillow)
fg_pil = Image.open("foreground.png").convert("RGB")
fg = np.array(fg_pil)
fg = cv2.cvtColor(fg, cv2.COLOR_RGB2BGR) # we convert rgb to bgr since OpenCV assumes bgr colors whereas Pillow uses rgb
#not necessary; if not done would just exchange blues with reds and so more like visual error and not logical error rest other things work fine

# 2. Background removal using GrabCut
# mask marks pixels, while bg_model and fg_model are internal memory used by GrabCut to learn what background and foreground look like.
#Create a 2D image (same height and width as the original image), filled with zeros, to store background/foreground labels.
mask = np.zeros(fg.shape[:2], np.uint8) # uint8: Data type = 8-bit unsigned integer;OpenCV expects masks in uint8
# Stores what the algorithm learns about the background
bg_model = np.zeros((1, 65), np.float64) # We do not choose 65 — OpenCV requires it; 64-bit floating point numbers;GrabCut uses probabilities and statistics
# Needs decimals, not whole numbers
# Stores what the algorithm learns about the foreground
fg_model = np.zeros((1, 65), np.float64)

# Define rectangle roughly around object
h, w = fg.shape[:2] # fg.shape → (height, width, channels);  [:2] → we only take height, width
rect = (10, 10, w - 20, h - 20) # (x, y, width, height) 
# Start 10 pixels from left; Start 10 pixels from top; Rectangle width = image width − 20; Rectangle height = image height − 20

# GrabCut: Treats everything outside rectangle as background; Treats everything inside rectangle as possible foreground
#Learns color patterns; Improves the separation 5 times
cv2.grabCut(fg, mask, rect, bg_model, fg_model, 5, cv2.GC_INIT_WITH_RECT)

# After grabcut mask has values as 0(Sure background), 1(Sure foreground), 2(Probably background), 3(Probably foreground)
# So we change it into binary mask 

# Create binary mask
# np.where(condition, 0, 1); If condition is true → put 0; Else → put 1
# So: Background → 0; Foreground → 1
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype("uint8") # .astype("uint8"): Converts values to 0 or 1 for openCV 

# Extract foreground
fg_extracted = fg * mask2[:, :, np.newaxis] # [:, :, np.newaxis]: Changes shape to:(height, width, 1)

# 3. Load background image
bg = cv2.imread("background.jpg")

# 4. Resize foreground if needed
new_width = 200
scale = new_width / fg_extracted.shape[1]
new_height = int(fg_extracted.shape[0] * scale)

fg_resized = cv2.resize(fg_extracted, (new_width, new_height))
mask_resized = cv2.resize(mask2, (new_width, new_height))

# 5. Choose position (x, y)
x, y = 100, 150  # top-left corner

# Ensure it fits inside background
h_fg, w_fg = fg_resized.shape[:2]
roi = bg[y:y+h_fg, x:x+w_fg]

# 6. Overlay using mask
mask_inv = cv2.bitwise_not(mask_resized * 255)

bg_part = cv2.bitwise_and(roi, roi, mask=mask_inv)
fg_part = cv2.bitwise_and(fg_resized, fg_resized, mask=mask_resized * 255)

final_roi = cv2.add(bg_part, fg_part)
bg[y:y+h_fg, x:x+w_fg] = final_roi

# 7. Display and save result

cv2.imshow("Final Result", bg)
cv2.imwrite("final_output.png", bg)
cv2.waitKey(0)
cv2.destroyAllWindows()