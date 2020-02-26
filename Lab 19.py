#Lab 19
#Nabeel Khan
#Nabeel.khan24@myhunter.cuny.edu
#March 5, 2020
#This program uses a turtle to draw a spiral

import turtle

steps = 20
stamps = int(input('Please enter the number of turtle stamps: '))
tess = turtle.Turtle()
tess.shape('turtle')
tess.penup()
for i in range(stamps):
    tess.stamp()
    steps += 2
    tess.forward(steps)
    tess.right(24)