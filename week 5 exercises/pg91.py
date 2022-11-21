Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> smaller = int(input("Enter the smaller number: "))
Enter the smaller number: 2
>>> larger = int(input("Enter the larger number: "))
Enter the larger number: 8
>>> myNumber = random.randint(smaller, larger)
>>> count = 0
>>> while True:
...     count += 1
...     userNumber = int(input("Enter your guess: "))
...     if userNumber < myNumber:
...         print("Too Small!")
...     elif userNumber < myNumber:
...         print("Too large!")
...     else:
...         print("Congratulations! You've got it in", count, "tries!")
...         break
... 
...     
Enter your guess: 1
Too Small!
Enter your guess: 2
Too Small!
Enter your guess: 3
Congratulations! You've got it in 3 tries!
