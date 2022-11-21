Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> height = float(input("Enter the height of the ball being dropped: "))
Enter the height of the ball being dropped: 25
>>> bounceIndex = float(input("Enter the balls bounciness index: "))
Enter the balls bounciness index: .9
>>> noBounces = int(input("Enter the number of times the ball bounces: "))
Enter the number of times the ball bounces: 5
>>> distance = height
>>> for i in range(noBounces-1):
...     height *= bounceIndex
...     distance += 2*height
... 
...     
>>> distance += height*bouncesIndex
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    distance += height*bouncesIndex
NameError: name 'bouncesIndex' is not defined. Did you mean: 'bounceIndex'?
>>> distance += height*bounceIndex
>>> print("\nTotal distance traveled is: " +str(distance) + ' feet.')

Total distance traveled is: 194.51725 feet.
