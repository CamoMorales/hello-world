Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> f = open("myfile.txt", 'r')
>>> text = f.read()
>>> text
'First line. \nSecond line.\n'
>>> print(text)
First line. 
Second line.

>>> f = open("myfile.txt", 'r')
>>> for line in f:
...     print(line)
... 
...     
First line. 

Second line.

