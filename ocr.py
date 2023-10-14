#usr/bin/ python3
import subprocess
from PIL import  ImageGrab
from paddleocr import PaddleOCR 
import os
import pyperclip

subprocess.run(["gnome-screenshot", "-a"]) 

ocr = PaddleOCR(use_angle_cls=True)

img_path=''
for filename in os.listdir('/home/shemol/Pictures/'):
    print(filename)
    root,ext = os.path.splitext(filename)
    if root.startswith('Screenshot') and ext=='.png':
        img_path='/home/shemol/Pictures/'+filename
        break

result = ocr.ocr(img_path, cls=True)

os.remove(img_path)

result = result[0]
txts = [line[1][0] for line in result]

contents = ""

for content in result:
    contents = contents + ' ' + content[1][0]

pyperclip.copy(contents)

