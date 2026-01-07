# Wids Project: Augmented Reality Face Tracking and Overlay System

## Overview
This repository contains all the coding work completed up to the midterm (week2).The project focuses on computer vision techniques used in an Augmented Reality Face Trackingand Overlay System.

## Content
- Face detection and facial landmark detection using MediaPipe
- Background removal using OpenCV (GrabCut)
- Image overlay techniques
- Video processing scripts

## Technologies Used
- Python
- OpenCV
- MediaPipe
- NumPy
- Pillow

## Week 0: Mini Image Editor
A Python script that performs basic image manipulation operations. The image is loaded using Pillow, converted to an OpenCV-compatible format,and processed based on user choice.
File: `week0.py`
- Load image using Pillow
- Convert image from RGB to BGR
- Resize image
- Sharpen image
- Display and save the final output

## Week 1: Background Removal and Object Overlay
A Python script that extracts a foreground object from an image and places it onto a new background image using OpenCV.
File: `w1.py`
- Load foreground image using Pillow
- Remove background using GrabCut or Semantic Segmentation
- Load a separate background image
- Resize the extracted object if required
- Overlay the object onto the background at chosen (x, y) coordinates
- Display and save the final result

## Week 2: Face Landmark Detection and AR Overlay
A Python script that applies an augmented reality overlay on a face in a video using facial landmark detection.
File: `w2.py`
- Load a face video
- Load an overlay image
- Detect facial landmarks using MediaPipe
- Apply overlay based on facial landmarks
- Display and save the processed video
