Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
salary = float(input("Enter the starting salary: "))
Enter the starting salary: 50000
percent = float(input("Enter the annual percent increase: "))
Enter the annual percent increase: 2
years = int(input("Enter the number of years: "))
Enter the number of years: 10
>>> for i in range(1, years+1):
...     print("Year        Salary")
...     print("==================")
...     print(i,"\t",end="")
...     print("%.2f"%salary)
...     salary = salary * (1+percent/100)
... 
...     
Year        Salary
==================
1 	50000.00
Year        Salary
==================
2 	51000.00
Year        Salary
==================
3 	52020.00
Year        Salary
==================
4 	53060.40
Year        Salary
==================
5 	54121.61
Year        Salary
==================
6 	55204.04
Year        Salary
==================
7 	56308.12
Year        Salary
==================
8 	57434.28
Year        Salary
==================
9 	58582.97
Year        Salary
==================
10 	59754.63
