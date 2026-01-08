#!/usr/bin/env python3
import glob
import os
import numpy as np
import cv2

# choose the Ratio here
targetRatio = 1 #4/5

# Decide whether to resize the final padded image to targetResolutions
downsize = True

targetResX = 1080
targetResY = 1080 if targetRatio == 1 else 1350

def pad_image_cv2(image_path, output_path, color=[255,255,255]):
    """
    Color is in BGR format by default for OpenCV.
    """
    img = cv2.imread(image_path)
    h, w = img.shape[:2]

    # Calculate padding needed to make it as necessary
    currentRatio = w/h

    # image is too wide, add vertically
    if currentRatio > targetRatio:
        newH = w / targetRatio
        newW = w
    # image too tall add horizontally
    else:
        newW = h * targetRatio
        newH = h

    left = int((newW-w) / 2)
    right = left
    top = int((newH-h) / 2)
    bottom = top

    # Add padding
    padded_img = cv2.copyMakeBorder(
        img, 
        top, 
        bottom, 
        left, 
        right, 
        cv2.BORDER_CONSTANT, 
        value=color
    )

    # Resize the final padded image to 1080x1080
    if downsize:
        final_img = cv2.resize(padded_img, (targetResX, targetResY), interpolation=cv2.INTER_AREA)
    else:
        final_img = padded_img 

    cv2.imwrite(output_path, final_img)
    #print(f"Image saved to {output_path}")


#change to pwd
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

#make new dir
dirName = 'instaReady'
if targetRatio == 1:
    dirName =+ '1x1'
else:
    dirName =+ '4x5'

os.makedirs(dirName, exist_ok=True)

# Pattern to find all files ending with .jpg or .jpeg (case-insensitive)
# The glob.glob() function returns a list of file paths that match the pattern.
jpeg_files = glob.glob('*.jpg') + glob.glob('*.jpeg')
# Optional: also include uppercase extensions
jpeg_files += glob.glob('*.JPG') + glob.glob('*.JPEG')

print(f"Found {len(jpeg_files)} JPEG files:")
# Iterate over the list of files
for file_name in jpeg_files:
    # Print the file name
    print(file_name)
    color=[255,255,255] #white
    pad_image_cv2(file_name, 'instaReady/'+file_name, color)

print(f"done")
