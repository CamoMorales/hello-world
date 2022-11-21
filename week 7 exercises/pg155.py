Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> info = {}
>>> info["name"] = "sandy"
>>> info["occupation"] = "hacker"
>>> info
{'name': 'sandy', 'occupation': 'hacker'}
>>> info["occupation"] = "manager"
>>> info
{'name': 'sandy', 'occupation': 'manager'}
>>> info["name"]
'sandy'
>>> info["job"]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    info["job"]
KeyError: 'job'
>>> if "job" in info:
...     print(info["job"])
... 
...     
>>> print(info.get("job", none))
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(info.get("job", none))
NameError: name 'none' is not defined. Did you mean: 'None'?
>>> print(info.get("job", None))
None
>>> print(info.pop("job", None))
None
>>> print(info.pop("occupation"))
manager
>>> info
{'name': 'sandy'}
>>> for key info:
...     
SyntaxError: invalid syntax
>>> for key in info
SyntaxError: expected ':'
>>> for key in info:
...     print(key, info[key])
... 
...     
name sandy
>>> grades = {90:'A', 80:'B', 70:'C'}
>>> list(grades.items())
[(90, 'A'), (80, 'B'), (70, 'C')]
>>> for (key, value) in grades. items():
...     print(key, value)
... 
...     
90 A
80 B
70 C
