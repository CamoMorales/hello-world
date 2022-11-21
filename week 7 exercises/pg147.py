Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def average(lyst):
...     """Returns the average of the numbers in lyst."""
...     theSum = 0
...     for number in lyst:
...         theSum += number
...     return theSum / len(lyst)
... 
>>> average([1, 3, 5, 7])
4.0
