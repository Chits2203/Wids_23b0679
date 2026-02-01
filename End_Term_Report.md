# Augmented Reality Face Tracking and Overlay System

## Abstract

This project implements a real-time Augmented Reality (AR) face tracking and overlay system using Python. The system detects facial landmarks from a live webcam feed and dynamically places a user-selected overlay image on different regions of the face such as the nose, forehead, eyes, or cheeks. The project integrates concepts from computer vision, image processing, and human–computer interaction using OpenCV, MediaPipe, Pillow, and NumPy. The final system supports background removal, real-time landmark tracking, adaptive resizing, and interactive placement control, demonstrating an end-to-end AR pipeline.

## 1. Introduction

Augmented Reality overlays digital content onto the real world in real time. Face-based AR is widely used in social media filters, virtual try-ons, and interactive entertainment. The goal of this project is to build a simplified yet functional AR face overlay system from scratch, while learning core computer vision concepts such as image manipulation, background removal, facial landmark detection, and real-time video processing.

The project is structured over multiple weeks, each focusing on a specific subproblem. By the final week, all components are merged into a complete working system.

## 2. Project Objectives

The main objectives of this project are:

* To understand image representations and basic image operations in Python
* To perform background removal from images
* To detect facial landmarks accurately in real time
* To overlay images on detected facial regions with correct scaling and positioning
* To design an interactive AR system using a webcam

## 3. Tools and Technologies Used

* **Python**: Core programming language
* **OpenCV (cv2)**: Image processing and webcam handling
* **MediaPipe**: Facial landmark detection (Face Mesh)
* **Pillow (PIL)**: Image loading and format conversion
* **NumPy**: Numerical operations and array manipulation
* **Tkinter**: File dialog for user-selected overlay images

## 4. Week-wise Development

### 4.1 Week 0: Python and Image Processing Basics

In the initial week, the focus was on revising Python fundamentals such as functions, lists, and package installation. NumPy was introduced to understand image arrays, indexing, slicing, and reshaping. Using Pillow and OpenCV, a mini image editor was created that could load an image, resize it, convert color spaces, apply sharpening, and save the output.

### 4.2 Week 1: Background Removal and Static Overlay

This stage focused on separating the foreground from the background. Two approaches were studied:

* Semantic Segmentation using Deep Learning
* GrabCut and color-threshold-based background removal

For the final system, a simple and efficient color thresholding technique was implemented to remove white or uniform backgrounds. The extracted object was then overlaid onto a different static background image using alpha blending.

### 4.3 Week 2: Facial Landmark Detection

MediaPipe Face Mesh was used to detect 468 facial landmarks from images and videos. This week focused on understanding landmark indices and mapping normalized landmark coordinates to pixel coordinates. The system was tested on pre-recorded face videos to ensure accurate landmark tracking.

### 4.4 Week 3: Real-Time Webcam Integration

The system was extended to real-time webcam input using OpenCV. Facial landmarks were detected live, and a fixed overlay image was placed on specific facial regions based on keyboard input. This step introduced real-time constraints and performance considerations.

### 4.5 Week 4: End-to-End AR Overlay System

In the final week, all components were combined into a single system. Users can upload their own overlay image, remove its background automatically, and place it dynamically on different facial regions in real time. The overlay resizes automatically based on face dimensions and selected placement.

## 5. System Architecture

The system follows a modular pipeline:

1. Webcam frame capture
2. Face landmark detection using MediaPipe
3. Overlay image loading and background removal
4. Landmark-based position and scale computation
5. Alpha blending overlay onto the frame
6. Real-time display and user interaction

## 6. Background Removal Method

The implemented background removal technique uses classic color thresholding. Pixels close to white are detected using RGB thresholds and removed by setting their alpha values to zero. Morphological erosion is applied to reduce noise. This approach is computationally efficient and suitable for uniform backgrounds.

## 7. Facial Landmark-Based Placement

Specific landmark indices are used to identify facial regions such as eyes, nose, mouth, ears, forehead, and chin. Distances like ear-to-ear and top-of-head to chin are used to adaptively scale the overlay image, ensuring consistent placement across different face sizes and camera distances.

## 8. User Interaction

The system provides keyboard-based interaction:

* `o` to upload a new overlay image
* Number keys (1–7) to change overlay placement
* `q` to quit the application

Supported placements include head, forehead, eyes, nose, mouth, chin, and both cheeks.

## 9. Results and Observations

The final system successfully overlays images in real time with stable tracking and adaptive resizing. The overlay remains aligned with facial movements such as rotation and translation. Minor jitter may occur under poor lighting or extreme head angles, which is a known limitation of landmark-based tracking.

## 10. Limitations

* Background removal works best for white or uniform backgrounds
* Performance depends on lighting conditions and webcam quality
* Only single-face tracking is supported

## 11. Future Scope

Possible improvements include:

* Using deep-learning-based background removal for complex images
* Supporting multiple faces
* Adding smoothing filters to reduce jitter
* Creating a GUI-based placement selector
* Extending to mobile or web-based AR systems

## 12. Conclusion

This project demonstrates a complete end-to-end AR face overlay system built using fundamental computer vision techniques. By progressively developing each component, the project provides a strong foundation in real-time image processing and AR concepts, closely resembling simplified versions of industry-level AR filters.

---

**End of Report**
