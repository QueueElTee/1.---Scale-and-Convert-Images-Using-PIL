import os
from PIL import Image

directory = 'images/'

for file in os.listdir(directory):
    if file.startswith('.'):
        continue
    im = Image.open(directory + file)
    im.convert("RGB").rotate(-90).resize((128, 128)).save("opt/icon/"+file+".jpeg")