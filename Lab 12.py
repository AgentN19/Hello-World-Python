#Lab 12
#Nabeel Khan
#Nabeel.khan24@myhunter.cuny.edu
#February 25, 2020
#This program draws a purple shape

import turtle
turtle.colormode(255)
tess = turtle.Turtle()
tess.shape("turtle")
tess.backward(100)

for i in range(0,255,10):
     tess.forward(10)
     tess.pensize(i)
     tess.color(i,0,i)