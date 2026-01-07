from PIL import Image
import cv2
import numpy as np

def load_image(path):
    # Load image using Pillow
    pil_image = Image.open(path).convert("RGB")
    # Convert to OpenCV format (NumPy array)
    cv_image = np.array(pil_image)
    return cv_image

def rgb_to_bgr(image):
    return cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

def resize_image(image, width, height):
    return cv2.resize(image, (width, height))

def sharpen_image(image):
    kernel = np.array([
        [0, -1,  0],
        [-1, 5, -1],
        [0, -1,  0]
    ])
    return cv2.filter2D(image, -1, kernel)

def main():
    image_path = input("Enter image path: ")
    image = load_image(image_path)

    print("\nChoose an operation:")
    print("1. Convert RGB to BGR")
    print("2. Resize")
    print("3. Sharpen")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        result = rgb_to_bgr(image)

    elif choice == "2":
        width = int(input("Enter new width: "))
        height = int(input("Enter new height: "))
        result = resize_image(image, width, height)

    elif choice == "3":
        result = sharpen_image(image)

    else:
        print("Invalid choice")
        return

    # Display image
    cv2.imshow("Edited Image", result)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

    # Save result
    output_path = "edited_image.jpg"
    cv2.imwrite(output_path, result)
    print(f"Image saved as {output_path}")

if __name__ == "__main__":
    main()
