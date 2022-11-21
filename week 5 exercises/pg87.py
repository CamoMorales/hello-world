Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> theSum = 0.0
>>> data = input("Enter a number or just enter to quit: ")
Enter a number or just enter to quit: 3
>>> while data != "":
...     number = float(data)
...     theSum += number
...     data = input("Enter a number or just enter to quit: ")
... 
...     
Enter a number or just enter to quit: 1
Enter a number or just enter to quit: 2
Enter a number or just enter to quit: 3
Enter a number or just enter to quit: 
>>> print("The sum is", theSum)
The sum is 9.0
