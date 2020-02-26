#Lab 4
#Nabeel Khan
#Nabeel.khan24@myhunter.cuny.edu
#February 11, 2020
#This program draws a flower

import turtle

tess = turtle.Turtle()

for i in range(150):
    tess.forward(0.5*i)
    tess.penup()
    tess.forward(0.5*i)
    tess.pendown()
    tess.left(110)