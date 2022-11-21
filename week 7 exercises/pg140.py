Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> example = [1, 2]
>>> example
[1, 2]
>>> example.append(3)
>>> example
[1, 2, 3]
>>> example.extend([11, 12, 13])
>>> example
[1, 2, 3, 11, 12, 13]
>>> example + [14, 15]
[1, 2, 3, 11, 12, 13, 14, 15]
>>> example
[1, 2, 3, 11, 12, 13]
>>> example.pop
<built-in method pop of list object at 0x000001B1EBDC3DC0>
>>> example.pop()
13
>>> example
[1, 2, 3, 11, 12]
>>> example.pop(0)
1
>>> example
[2, 3, 11, 12]
>>> 
================ RESTART: C:/Users/Mason/AppData/Local/Programs/Python/Python310/searchalist.py ================
1
