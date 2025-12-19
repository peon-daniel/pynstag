#pyinstaller.exe --onefile  pynstag.py
import glob
import os
import numpy as np
import cv2


def pad_image_cv2(image_path, output_path, color=[255,255,255]):
    """
    Color is in BGR format by default for OpenCV.
    target: 1080x1350
    """
    img = cv2.imread(image_path)
    h, w = img.shape[:2]

    # Calculate padding needed to make it 4:5

    targetRatio = 4/5
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
    final_img = cv2.resize(padded_img, (1080, 1350), interpolation=cv2.INTER_AREA)

    cv2.imwrite(output_path, final_img)
    #print(f"Image saved to {output_path}")


#change to pwd
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

#make new dir
os.makedirs('instaReady', exist_ok=True)

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
