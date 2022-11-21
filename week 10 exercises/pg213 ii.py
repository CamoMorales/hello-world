Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from polygons import *
>>> from turtle import Turtle
>>> t = Turtle()
>>> t.pencolor("blue")
>>> t.hideturtle()
>>> square(t, 50)
>>> hexagon(t, 50)
>>> t.clear()
>>> radialHexagons(t, 10, 50)
