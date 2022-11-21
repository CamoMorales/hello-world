Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from turtle import Turtle
>>> import random
>>> 
>>> def randomWalk(t, turns, distance = 20):
...     """Turns a random number of degrees and moves a given
...     distance for a fixed number of turns."""
...     for x in range(turns):
...         if x % 2 == 0:
...             t.left(random.randint(0, 270))
...         else:
...             t.right(random.randint(0, 270))
...             t.forward(distance)
... 
...             
>>> def main():
...     t = Turtle()
...     t.shape("turtle")
...     randomWalk(t, 40, 30)
... 
...     
>>> if __name__ == "__main__":
...     main()
... 
...     
