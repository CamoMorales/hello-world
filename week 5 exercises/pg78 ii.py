Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> area = float(input("Enter the area: "))
Enter the area: 0
>>> if area > 0:
...     radius = math.sqrt(area / math.pi)
...     print("The radius is". radius)
... else:
...     print("Error: the area must be a positive number")
... 
...     
Error: the area must be a positive number
