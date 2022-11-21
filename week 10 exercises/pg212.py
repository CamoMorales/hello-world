Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def square(t, length):
...     """Draws a square with given length."""
...     for count in range(4):
...         t.forward(length)
...         t.left(90)
... 
...         
>>> square
<function square at 0x000001FF46D913A0>
>>> square(t, 100)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    square(t, 100)
NameError: name 't' is not defined
>>> def hexagon(t, length):
...     """Draws a hexagon with the given length."""
...     for count in range(6):
...         t.forward(length)
...         t.left(60)
... 
...         
>>> hexagon(t, 100)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    hexagon(t, 100)
NameError: name 't' is not defined
