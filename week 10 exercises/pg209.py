Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def drawSquare(t, x, y, length):
...     """Draws a square with the given turtle t, an upper-left
...     corner point (x, y), and a side's length."""
...     t.up()
...     t.goto(x, y)
...     t.setheading(270)
...     t.down()
...     for count in range(4):
...         t.forward(length)
...         t.left(90)
... 
...         
>>> drawSquare(t, 100, 100, 100)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    drawSquare(t, 100, 100, 100)
NameError: name 't' is not defined
