Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name = "Alan Turing"
>>> name[0]
'A'
>>> name[3]
'n'
>>> name[len(name)]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    name[len(name)]
IndexError: string index out of range
>>> name[len(name) - 1]
'g'
>>> name[-1]
'g'
>>> name[-2]
'n'
