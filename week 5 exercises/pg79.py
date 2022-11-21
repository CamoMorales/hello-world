Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> first = int(input("Enter the first number: "))
Enter the first number: 1
>>> second = int(input("Enter the second number: "))
Enter the second number: 2
>>> if first > second:
...     maximum = first
...     minimum = second
... else:
...     maximum = second
...     minimum = first
... 
...     
>>> print("Maximum:", maximum)
Maximum: 2
>>> print("Minimum:", minimum)
Minimum: 1
>>> 
>>> first = int(input("Enter the first number: "))
Enter the first number: 1
>>> second = int(input("Enter the second number: "))
Enter the second number: 2
>>> print("Maximum:", max(first, second))
Maximum: 2
>>> print("Minimum": min(first, second))
SyntaxError: invalid syntax
>>> print("Minimum", min(first, second))
Minimum 1
