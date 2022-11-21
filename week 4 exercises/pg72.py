Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for exponent in range(7, 11):
...     print("%-3d%12d" % (exponent, 10 ** exponent))
... 
...     
7      10000000
8     100000000
9    1000000000
10  10000000000
>>> salary = 100.00
>>> print("Your salary is $" + str(salary))
Your salary is $100.0
>>> print("Your salary is $0.2f % salary)
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print("Your salary is $%0.2f" % salary)
...       
Your salary is $100.00
>>> "%6.3f" % 3.14
...       
' 3.140'
