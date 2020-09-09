#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightpink")
panel.bgpic(image)

#=======Add your code here======



t = Turtle()
t.pencolor("blue")
t.pensize(10)
t.forward(100)
t.left(90)
t.forward(225)
t.left(90)
t.forward(200)
t.left(90)
t.forward(225)
t.left(90)
t.forward(100)

t.penup()
t.goto(-200,-200)
t.pensize(4)
t.pendown()
t.color("purple", "green")
t.begin_fill()
t.circle(50)
t.end_fill()

t.penup()
t.goto(200,-200)
t.pensize(7)
t.pendown()
t.pencolor("yellow")
t.forward(75)
t.left(45)
t.forward(75)
t.left(45)
t.forward(75)
t.left(45)
t.forward(75)
t.left(45)
t.forward(75)
t.left(45)
t.forward(75)
t.left(45)
t.forward(75)
t.left(45)
t.forward(75)

t.penup()
t.goto(-400,0)
t.pensize(13)
t.pendown()
t.pencolor((100,150,200))
t.left(45)
t.forward(900)










