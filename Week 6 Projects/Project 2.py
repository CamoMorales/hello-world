Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> encryption = input("Enter the coded text: ")
Enter the coded text: ^1sjvtl'L}1yvul(
>>> distanceValue = int(input("Enter the distance value: "))
Enter the distance value: 7
>>> plainText = ""
>>> for ch in encryption:
...     ordvalue = ord(ch)
...     cipherValue = ordvalue - distanceValue
...     plainText += chr(cipherValue)
... 
...     
>>> print(plainText)
W*lcome Ev*rone!
