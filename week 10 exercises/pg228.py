Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from images import Image
>>> image = Image(150, 150)
>>> image.draw()
>>> blue = (0, 0, 255)
>>> y = image.getHeight() // 2
>>> for x in range(image.getWidth()):
...     image.setPixel(x, y - 1, blue)
...     image.setPixel(x, y, blue)
...     image.setPixel(x, y + 1, blue)
... 
...     
>>> image.draw()
