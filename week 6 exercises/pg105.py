Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name = "myfile.txt"
>>> name[0:]
'myfile.txt'
>>> name[0:1]
'm'
>>> name[0:2]
'my'
>>> name[:len(name)]
'myfile.txt'
>>> name[-3:]
'txt'
>>> name[2:6]
'file'
