Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> f = open("myfile.txt", 'r')
>>> while True:
...     line = f.readline()
...     if line == "":
...         break
...     print(line)
... 
...     
First line. 

Second line.

>>> f = open("intergers.txt", 'r')
>>> theSum = 0
>>> for line in f:
...     line = line.strip()
...     number = int(line)
...     theSum += number
... 
...     
>>> print("The sum is", theSum)
The sum is 0
