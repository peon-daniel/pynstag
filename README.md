# pynstaG

This utility is meant to pad all the jpeg files in the current directory to make them 1:1 (square) or 4:5 with resolution 1080px by 1350, because this is the maximum allowed on instagram at the moment.

Just instruct windows to execute *.py files with python.exe or add a #!/usr/bin/env python3 shebang on mac/linux and make executable.

It will automatically create a folder named 'instaReady' with your padded low-res versions there.

## Requirements

`pip install opencv-python`
