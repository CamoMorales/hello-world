Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = int(input("Enter the first side: "))
Enter the first side: 4
>>> y = int(input("Enter the second side: "))
Enter the second side: 4
>>> z = int(input("Enter the third side: "))
Enter the third side: 2
>>> if ((x * x + y * y == z * z) or (y * y + z * z == x * x) or (z * z + x * x == y * y)):
...     print("The triangle is a right triangle")
... else:
...     print("The triangle is not a right triangle")
... 
...     
The triangle is not a right triangle
