Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> hourlyWages = float(input("Enter the hourly wage: "))
Enter the hourly wage: 20
>>> normalHours = float(input("Enter the normal hours: "))
Enter the normal hours: 80
>>> overHours = float(input("Enter the overtime hours: "))
Enter the overtime hours: 4
>>> biweeklyPay = (hourlyWages * normalHours) + (1.5 * hourlyWages * overHours)
>>> print(biweeklyPay)
1720.0
