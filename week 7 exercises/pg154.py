Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> info = {}
>>> info["name"] = "sandy"
>>> info["occupation"] = "manager"
>>> info
{'name': 'sandy', 'occupation': 'manager'}
>>> info["name"]
'sandy'
>>> info["job"]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    info["job"]
KeyError: 'job'
