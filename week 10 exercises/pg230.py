Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from images import Image
>>> image = Image("smokey.gif")
>>> (r, g, b) = image.getPixel(0, 0)
>>> r
194
>>> g
221
b
>>> 
>>> image.setPixel(0, 0, (r + 10, g + 10, b + 10))
>>> def average(triple):
...     (a, b, c) = triple
...     return (a + b + c) // 3
... 
>>> average((40, 50, 60))
50
