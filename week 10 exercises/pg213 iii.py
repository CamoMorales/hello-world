Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from polygons import *
>>> from turtle import Turtle
>>> t = Turtle()
>>> def radialPattern(t, n, length, shape):
...     """Draws a radial pattern of n shapes with the given length."""
...     for count in range(n):
...         shape(t, length)
...         t.left(360 / n)
... 
...         
>>> t = Turtle()
>>> radialPattern(t, n = 10, length = 50, shape = square)
t.clear()
>>> t.clear()
>>> radialPattern(t, n = 10, length = 50, shape = hexagon)
