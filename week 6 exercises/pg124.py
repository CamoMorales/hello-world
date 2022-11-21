Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
>>> currentDirectoryPath = os.getcwd()
>>> listOfFileNames = os.listdir(currentDirectoryPath)
>>> for name in listOfFileNames:
...     if ".py" in name:
...         print(name)
... 
...         
binarytodecimal.py
decimaltobinary.py
decrypt.py
encrypt.py
page 112 week 6.py
