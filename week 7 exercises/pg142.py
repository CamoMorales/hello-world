Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> first = [10, 20, 30]
>>> second = first
>>> first
[10, 20, 30]
>>> second
[10, 20, 30]
>>> first[1] = 99
>>> first
[10, 99, 30]
>>> second
[10, 99, 30]
>>> third = []
>>> for element in first:
...     third.append(elements)
... 
...     
Traceback (most recent call last):
  File "<pyshell#10>", line 2, in <module>
    third.append(elements)
NameError: name 'elements' is not defined. Did you mean: 'element'?
>>> third = []
>>> for element in first:
...     third.append(element)
... 
...     
>>> first
[10, 99, 30]
>>> third
[10, 99, 30]
>>> first[1] = 100
>>> first
[10, 100, 30]
>>> third
[10, 99, 30]
