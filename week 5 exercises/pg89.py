Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> theSum = 0.0
>>> while True:
...     data = input("Enter a number or just enter to quit: ")
...     if data == "":
...         break
...     number = float(data)
...     theSum += number
... 
...     
Enter a number or just enter to quit: 2
Enter a number or just enter to quit: 3
Enter a number or just enter to quit: 4
Enter a number or just enter to quit: 
>>> print("The sum is", theSum)
The sum is 9.0
