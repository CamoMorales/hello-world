Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> while True:
...     number = int(input("Enter the numeric grade: "))
...     if number >= 0 and number <= 100:
...         break
...     else:
...         print("Error: grade must be between 100 and 0")
... 
...         
Enter the numeric grade: 110
Error: grade must be between 100 and 0
Enter the numeric grade: -1
Error: grade must be between 100 and 0
Enter the numeric grade: 45
>>> print(number)
45
