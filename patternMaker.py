from turtle import *
from random import randint

def drawShape(sides,length,outline,fill):
    begin_fill()
    color(outline,fill)
    penup()
    pendown()
    for n in range (0,sides):
        forward(length)
        right(360/sides)
    penup()
    end_fill()

print("be sensible with the length of the sides and angle")
numOfSides = input("number of sides?")
lengthOfSides = input("length of sides?")
outlineColour = input("outline colour?")
fillColour = input("fill colour?")
angleStep = input("rotation between shape?")

numOfSides = int(numOfSides)
lengthOfSides = int(lengthOfSides)
angleStep = int(angleStep)


for i in range(0,360,angleStep):
     drawShape(numOfSides,lengthOfSides,outlineColour,fillColour)
     right(angleStep)
