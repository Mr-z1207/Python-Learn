# pillow
from PIL import Image, ImageFilter
img = Image.open('000test/045_常用内建模块-HTMLParser.png')

w, h = img.size
print('Original image size: %sx%s' % (w, h))

# 缩放到50%:
img.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))

# 把缩放后的图像用jpeg格式保存:
# img.save('./000test/046_test.png', 'png')

img2 = img.filter(ImageFilter.BLUR)
# img2.save('./000test/046_test.png', 'png')
