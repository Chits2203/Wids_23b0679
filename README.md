# Augmented Reality Face Tracking & Overlay System  
**WiDS Mid-Term Project**

## Student Details
- **Name:** Prachi Arya  
- **Roll Number:** 23B0679  
- **Date of Submission:** January 7, 2026  

---

## Project Overview
This repository contains all the coding work completed up to the midterm for the WiDS project
titled **“Augmented Reality Face Tracking & Overlay System.”**

The objective of this project is to understand and implement core computer vision techniques
required for augmented reality applications, progressing step by step from basic image
manipulation to facial landmark–based AR overlays.

The work is divided into weekly deliverables (Week 0 to Week 2), each focusing on a specific
set of concepts and implementations.

---

## Week 0: Mini Image Editor

### Description
The Week 0 deliverable is a Python-based mini image editor. The script loads an image using
Pillow, converts it into an OpenCV-compatible NumPy array, and performs basic image
manipulations based on user choice.

### Features Implemented
- Loading images using Pillow (PIL)
- Conversion between RGB and BGR color spaces
- Image resizing using interpolation
- Image sharpening using convolution kernels
- Displaying and saving the processed output image

### Key Concepts Used
- Python fundamentals and modular programming
- NumPy arrays for image representation
- Color space conversion
- Basic image filtering and resizing using OpenCV

---

## Week 1: Background Removal and Image Overlay

### Description
The Week 1 deliverable focuses on foreground extraction and image compositing, which are
essential steps in augmented reality systems.

A foreground image is loaded and its background is removed using the GrabCut algorithm.
The extracted object is then resized and overlaid onto a new background image at a manually
chosen location.

### Features Implemented
- Loading foreground and background images using Pillow
- Background removal using the GrabCut algorithm
- Binary mask generation for foreground extraction
- Resizing the extracted foreground object
- Overlaying the object onto a new background using OpenCV
- Displaying and saving the final composited image

### Key Concepts Used
- Image segmentation
- GrabCut algorithm
- Masking and bitwise operations
- Image overlay and compositing

---

## Week 2: Facial Landmark Detection and AR Overlay

### Description
The Week 2 deliverable implements a facial landmark–based augmented reality pipeline on a
pre-recorded video.

The script loads a face video and an overlay image, detects facial landmarks using MediaPipe,
and places the overlay dynamically based on landmark positions. The processed video is then
displayed and saved.

### Features Implemented
- Loading and processing video frames using OpenCV
- Facial landmark detection using MediaPipe Face Landmarker
- Conversion of normalized landmark coordinates to pixel coordinates
- Overlay placement based on facial landmarks
- Alpha blending for smooth integration
- Saving the final output video

### Key Concepts Used
- Video processing
- Facial landmark detection
- Augmented reality overlays
- Alpha blending

---

## Technologies Used
- Python  
- OpenCV  
- Pillow (PIL)  
- NumPy  
- MediaPipe  

---

## Repository Structure
The repository is organized week-wise.  
Each week contains:
- Python scripts
- Sample input files
- Corresponding output files for demonstration

---

## Notes
This repository includes **only the work completed up to the midterm evaluation**, as required.
The implementations demonstrate a progressive understanding of computer vision concepts
leading to a functional augmented reality face tracking and overlay system.
