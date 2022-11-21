Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> f = open("intergers.txt", 'r')
>>> theSum = 0
>>> for line in f:
...     wordlist = line.split()
...     number = int(word)
...     theSum += number
... 
>>> print("The sum is, theSum)
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print("The sum is", theSum)
...       
The sum is 0
