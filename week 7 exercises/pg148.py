Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def odd(x)
SyntaxError: expected ':'
>>> def odd(x):
...     """Returns True if x is odd of False otherwise."""
...     if x % 2 == 1:
...         return True
...     else:
...         return False
... 
...     
>>> odd(5)
True
>>> odd(6)
False
