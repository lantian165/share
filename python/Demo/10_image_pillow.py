#/usr/bin/env python
# -*- coding: utf-8 -*-

# sudo pip install pillow
from PIL import Image, ImageFilter

# 打开一个图像
im = Image.open('/Users/zcy/Downloads/1.jpeg')

# 获得图像的尺寸
w, h = im.size

print 'Pict 1.png: w=%s, h=%s' %(w, h)

im2 = im.filter(ImageFilter.BLUR)

im2.save('./1-Blur.jpeg')

from PIL import Image, ImageFilter, ImageFont,  ImageDraw
import random

# 随机字母:
def rndChar():
    return chr(random.randint(65,90))

# 随机颜色:
def rndColor():
    return( random.randint(100,200), random.randint(100,200), random.randint(100,200))

def rndCorlr2():
    return( random.randint(80,126), random.randint(80,126), random.randint(80,126) )

# Picture size: 60 * 240
heigth = 60*4
width =  heigth * 4

# 创建一个图片文件
image = Image.new( 'RGB', (width, heigth), (255,255,255) )

# 创建 Font对象
font = ImageFont.truetype( 'Arial.ttf', 36 * 4 )

# 创建 Draw对象
draw = ImageDraw.Draw(image)

# 填充每个像素
for x in range(width):
    for y in range(heigth):
        draw.point((x,y),fill=rndColor())
        # draw.point((x,y),fill=(125,125,125))

# 输出文字
for i in range(4):
    draw.text(( 10 + i * 60 * 4, 10), rndChar(), font=font, fill=rndCorlr2() )

# 模糊
for i in range(3):
    image = image.filter(ImageFilter.BLUR)

image.save('./code.jpg', 'jpeg')

