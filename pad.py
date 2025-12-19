import cv2
import numpy as np


def pad_image_cv2(image_path, output_path, color=[255,255,255]):
    """
    Pads an image to a square format using OpenCV.
    Color is in BGR format by default for OpenCV.

    target: 1080x1350 size

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




    # #portrait mode
    # if h > w:
    #     # standard case in portrait mode
    #     if w/h < 4/5:
    #         diff = h - w
    #         left = diff // 2
    #         right = diff - left
    #         top, bottom = 0, 0
    #     # exception case in portrait ie 4:4.5, we still need to pad top and bottom
    #     else:

    # elif w > h:
    #     diff = w - h
    #     top = diff // 2
    #     bottom = diff - top
    #     left, right = 0, 0
    # else:
    #     top, bottom, left, right = 0, 0, 0, 0

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
    print(f"Image saved to {output_path}")

# Example usage:
# pad_image_cv2('your_photo.jpg', 'instagram_photo_cv2.jpg')