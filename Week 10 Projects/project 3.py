from turtle import Turtle
import math

import sys

def drawKochFractal(height, width, size, level):
    """Draws a Koch fractal of the given size and level."""
    t = Turtle()
    t.hideturtle()
    t.up()
    t.goto(width // 3, height // 4)
    t.down()

    drawFractalLine(t, size, 0, level);
    drawFractalLine(t, size, -120, level)
    drawFractalLine(t, size, 120, level)

def drawFractalLine(t, distance, theta, level):
    """Can draw a single line in a certain direction or four fractal
    lines in new directions."""
    if (level == 0):
        drawPolarLine(t, distance, theta)
    else:
        drawFractalLine(t, distance // 3, theta, level - 1)
        drawFractalLine(t, distance // 3, theta + 60, level - 1)
        drawFractalLine(t, distance // 3, theta - 60, level - 1)
        drawFractalLine(t, distance // 3, theta, level - 1)

drawPolarLine(t, distance, theta):
    """Moves a distance in a given direction."""
    t.setheading(theta)
    t.forward(distance)

def main():
    level = int(input("Enter the level: "))
    drawKochFractal(200, 200, 150, level)
