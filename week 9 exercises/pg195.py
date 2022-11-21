Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> abs
<built-in function abs>
>>> import math
>>> math.sqrt
<built-in function sqrt>
>>> f = abs
>>> f
<built-in function abs>
>>> f(-4)
4
>>> funcs = [abs, math.sqrt]
>>> funcs
[<built-in function abs>, <built-in function sqrt>]
>>> funcs[1](2)
1.4142135623730951
