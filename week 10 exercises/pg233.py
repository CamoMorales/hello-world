Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def grayscale(image):
...     """Converts the argument image to grayscale."""
...     for y in range(image.getHeight()):
...         for x in range(image.getWidth()):
...             (r, g, b) = image.getPixel(x, y)
...             r = int(r * 0.299)
...             g = int(g * 0.587)
...             b = int(b * 0.114)
...             lum = r + b + g
...             image.setPixel(x, y, (lum, lum, lum))
... 
...             
>>> from images import Image
>>> image = Image("smokey.gif")
>>> iamge.draw()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    iamge.draw()
NameError: name 'iamge' is not defined. Did you mean: 'image'?
>>> image.draw()
newImage = image.clone()
>>> newImage = draw()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    newImage = draw()
NameError: name 'draw' is not defined
>>> grayscale(newImage)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    grayscale(newImage)
NameError: name 'newImage' is not defined
>>> newImage.draw()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    newImage.draw()
NameError: name 'newImage' is not defined
