#Lab 3
#Nabeel Khan
#Nabeel.khan24@myhunter.cuny.edu
#Februar 10,2020
#This program draws a blue square and a triangle on a pink background

import turtle

wn = turtle.Screen()
wn.bgcolor("pink")

tess = turtle.Turtle()
tess.color("blue")
tess.pensize(5)

alex = turtle.Turtle()

for i in range(4):
    tess.forward(80)
    tess.left(90)
tess.left(180)
tess.forward(80)

for i in range(3):
    alex.forward(50)
    alex.left(120)

wn.exitonclick()