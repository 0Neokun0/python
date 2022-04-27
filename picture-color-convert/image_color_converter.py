import os
from PIL import Image

current_dirname = os.path.dirname(__file__) + '\\'
image = Image.open(current_dirname + 'files/flower01.jpg')
image.show()

# RGBごとに分離しています。
r, g, b  = image.split()

# RGB → BGR に置き換え
# 赤と青を入れ替えて合体(merge)している
convert_image = Image.merge("RGB", (b, g, r))

# 変換後の画像保存
convert_image.save(current_dirname + 'files/flower01_convert.jpg')
convert_image.show()