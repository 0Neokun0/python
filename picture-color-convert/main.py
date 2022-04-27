import os
from PIL import Image

current_dirname = os.path.dirname(__file__) + '\\'
image = Image.open(current_dirname + 'files/flower01.jpg')
image.show()
r, g, b  = image.split()
convert_image = Image.merge("RGB", (b, g, r))
convert_image.save(current_dirname + 'files/flower01_convert.jpg')
convert_image.show()