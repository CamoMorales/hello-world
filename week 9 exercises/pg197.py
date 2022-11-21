Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def odd(n): return n % 2 == 1
... 
>>> list(filter(odd, range(10)))
[1, 3, 5, 7, 9]
