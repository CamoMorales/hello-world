Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def hexagon(t, length):
...     """Draws a hexagon with the given length."""
...     for count in range(6):
...         t.forward(length)
...         t.left(60)
... 
...         
>>> def radialHexagons(t, n, length):
...     """Draws a radial pattern of n hexagons with the given length."""
...     for count in range(n):
...         hexagon(t, length)
...         t.left(360 / n)
... 
...         
>>> radialHexagons(t, 9, 100)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    radialHexagons(t, 9, 100)
NameError: name 't' is not defined
