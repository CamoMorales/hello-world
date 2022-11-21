Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> profit = 1000.55
>>> print('$' + profit)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print('$' + profit)
TypeError: can only concatenate str (not "float") to str
>>> print('$' + str(profit))
$1000.55
