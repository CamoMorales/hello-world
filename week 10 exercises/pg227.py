Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from images import Image
>>> image = Image("smokey.gif")
>>> image.draw()
>>> image.getWidth()
198
>>> image.getHeight()
149
>>> print(image)
File name: smokey.gif
Width:  198
Height: 149
>>> image.getPixel(0, 0)
(194, 221, 114)
