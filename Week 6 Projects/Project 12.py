Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> filename = input('Enter input filename: ')
Enter input filename: data.txt
>>> f = open(filename, 'r')
>>> print('{:<12s} {:>10s} {:>10s}'.format('Name', 'Hours', 'Total Pay'))
Name              Hours  Total Pay
>>> for line in f.readlines():
...     lname, hours, wage = line.split()
...     hours = int(hours)
...     wage = float(wage)
...     total = hours * wage
...     print('{:<12s} {:>10d} {:>10.2f}'.format(lname, hours, total))
... 
...     
John                 34    3366.00
Ryan                 30    2700.00
Sean                 34    3366.00
