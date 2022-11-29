Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> import turtle
>>> def drawCircle(t, x, y, radius):
...     t.up()
...     t.setposition(x, y)
...     t.forward(radius)
...     t.left(90)
...     t.down()
...     Circumference = ((2 * math.pi * radius) / 120)
...     i = 0
...     while i <= 120:
...         t.left(3)
...         t.forward(Circumference)
...         i += 1
... 
...         
>>> def main():
...     t = turtle.Turtle()
...     x=50
...     y=75
...     radius = 100
...     drawCircle(t, x, y, radius)
... 
...     
>>> main()
