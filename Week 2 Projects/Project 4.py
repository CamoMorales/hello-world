Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> radius = float(input("Enter the radius of the sphere: "))
Enter the radius of the sphere: 20
>>> dia = 2*radius
>>> cir = dia*math.pi
>>> surA = 4*math.pi*(radius**2)
>>> vol = (4/3)*math.pi*(radius**3)
>>> print("Diameter       :", dia)
Diameter       : 40.0
>>> print("Circumference: ", cir)
Circumference:  125.66370614359172
>>> print("Surface area: ", surA)
Surface area:  5026.548245743669
>>> print("Volume:", vol)
Volume: 33510.32163829113
