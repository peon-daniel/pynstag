#pyinstaller.exe --onefile  pynstag.py
import glob
import os
import numpy as np
from pad import pad_image_cv2



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

    # Example of what you can do with each file:
    # Get the absolute path
    # absolute_path = os.path.abspath(file_name)
    # print(f"Processing: {absolute_path}")
    
    # You can open the file, process the image, etc.
    # with open(file_name, 'rb') as f:
    #     pass 

    color=[255,255,255] #white
    pad_image_cv2(file_name, 'instaReady/'+file_name, color)