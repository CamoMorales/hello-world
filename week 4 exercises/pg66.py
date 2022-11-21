Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> number = 2
>>> exponent = 3
>>> product = 1
>>> for eachPass in range(exponent):
...     product = product * number
...     print(product, end = " ")
... 
...     
2 4 8 
>>> product
8
>>> for count in range(4):
...     print(count, end = " ")
... 
...     
0 1 2 3 
>>> product = 1
>>> for count in range(4):
...     product = product * (count + 1)
...     product
... 
...     
1
2
6
24
