Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> iterations = int(input("Enter the number of iterations: "))
Enter the number of iterations: 7
>>> piFour = 0;
>>> iterationCounter = 1;
>>> for i in range(1, iterations+1):
...     if(i % 2 != 0):
...         piFour = piFour + 1 /iterationCounter;
...     else:
...         piFour = piFour - 1 /iterationCounter;
...     iterationCounter = iterationCounter + 2;
... 
...     
>>> piValue = piFour*4;
>>> print(piValue,math.pi,sep='\n')
3.2837384837384844
3.141592653589793
