import cv2
import mediapipe as mp
import numpy as np
import os

# name of the image file
filename = "overlay.png"

# function to make a red circle if the picture is missing
def make_fake_picture():
    # make a blank clear box
    blank_box = np.zeros((100, 100, 4), dtype=np.uint8)
    # draw a red circle inside it
    cv2.circle(blank_box, (50, 50), 45, (0, 0, 255, 255), -1) 
    return blank_box

# checking if the file actually exists
if os.path.exists(filename):
    sticker = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
    # checking if it has 3 channels (normal) or 4 (transparent)
    if sticker.shape[2] == 3:
        # change it to include transparency
        sticker = cv2.cvtColor(sticker, cv2.COLOR_BGR2BGRA)
else:
    print("Could not find the image. Making a red circle instead.")
    sticker = make_fake_picture()

# make the sticker smaller
sticker = cv2.resize(sticker, (80, 80))

# setting up the google mediapipe tool
mp_face = mp.solutions.face_mesh
my_face_mesh = mp_face.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# dictionary to hold the numbers for different face parts
face_points = {
    "forehead": 10,
    "nose": 1,
    "mouth": 13
}

# starting position
location = "nose"

# function to put the sticker on top of the webcam video
def put_sticker_on_image(main_picture, sticker_image, x_pos, y_pos):
    
    # get the size of the background
    screen_h, screen_w, _ = main_picture.shape
    # get the size of the sticker
    sticker_h, sticker_w, _ = sticker_image.shape

    # make sure we don't go off the left or top edge
    start_x = max(x_pos, 0)
    start_y = max(y_pos, 0)
    
    # make sure we don't go off the right or bottom edge
    end_x = min(x_pos + sticker_w, screen_w)
    end_y = min(y_pos + sticker_h, screen_h)

    # if the sticker is totally off screen, just return the normal picture
    if start_x >= end_x or start_y >= end_y:
        return main_picture

    # math to cut the sticker image correctly
    sticker_start_x = start_x - x_pos
    sticker_start_y = start_y - y_pos
    sticker_end_x = sticker_start_x + (end_x - start_x)
    sticker_end_y = sticker_start_y + (end_y - start_y)

    # cutting out the pieces we need
    sticker_cutout = sticker_image[sticker_start_y:sticker_end_y, sticker_start_x:sticker_end_x]
    background_cutout = main_picture[start_y:end_y, start_x:end_x]

    # doing the blending magic
    alpha = sticker_cutout[:, :, 3] / 255.0
    inverse_alpha = 1.0 - alpha

    for c in range(3): # loop through colors
        background_cutout[:, :, c] = (alpha * sticker_cutout[:, :, c] + 
                                      inverse_alpha * background_cutout[:, :, c])

    # put the blended part back into the main picture
    main_picture[start_y:end_y, start_x:end_x] = background_cutout
    return main_picture

# start the webcam
webcam = cv2.VideoCapture(0)

print("Press 1 for Forehead, 2 for Nose, 3 for Mouth. Press q to quit.")

while webcam.isOpened():
    success, picture = webcam.read()
    if not success:
        break

    # flip the video like a mirror
    picture = cv2.flip(picture, 1)
    
    # change color for mediapipe
    color_picture = cv2.cvtColor(picture, cv2.COLOR_BGR2RGB)
    results = my_face_mesh.process(color_picture)

    # if a face is found
    if results.multi_face_landmarks:
        for face in results.multi_face_landmarks:
            h, w, _ = picture.shape
            
            # find which point number to use
            point_number = face_points[location]
            landmark = face.landmark[point_number]
            
            # math to find the x and y on the screen
            center_x = int(landmark.x * w)
            center_y = int(landmark.y * h)
            
            # adjust so the sticker is centered
            final_x = center_x - sticker.shape[1] // 2
            final_y = center_y - sticker.shape[0] // 2

            # call the function to draw the sticker
            picture = put_sticker_on_image(picture, sticker, final_x, final_y)

    # show the window
    cv2.imshow("My Face App", picture)

    # check for key presses
    key_pressed = cv2.waitKey(1) & 0xFF
    if key_pressed == ord('1'):
        location = "forehead"
    elif key_pressed == ord('2'):
        location = "nose"
    elif key_pressed == ord('3'):
        location = "mouth"
    elif key_pressed == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()