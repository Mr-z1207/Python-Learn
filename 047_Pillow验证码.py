# pillow
from PIL import Image, ImageFilter, ImageDraw, ImageFont

# 引入随机数
import random


# 随机字母:
def rndChar():
    # chr()返回值是当前整数对应的 ASCII 字符。
    return chr(random.randint(65, 90))


# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


# 设置宽高240 x 60:
width = 60 * 4
height = 60

# 首先创建一个图片或者打开一个图片
image = Image.new('RGB', (width, height), (255, 255, 255))

# 创建Font对象:
font = ImageFont.truetype('C:\\Windows\\Fonts\\simsunb.ttf', 36)
# 创建Draw对象:  创建一个可用来Image操作的对象(必须)
draw = ImageDraw.Draw(image)

# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())

# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())

image.save('code.jpg', 'jpeg')
