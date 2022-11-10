#idea of project- DRAWING USING TURTLE FOR FUN OR CHECK KEY AND HAND MOVEMENTS WHILE USING WASD AND C (for circle) 
#and r,g,b,y,o,v,i & p for color :D
#use e for eraser and over lap it :D 

import random
import turtle
import pyautogui as pg


bg=pg.confirm('Background Color',title='BG',buttons=['Black','Blue','Violet','Red','Green','Yellow'])



wn = turtle.Screen()
wn.title("TURTLE DRAWING")
wn.bgcolor(bg)
wn.setup(width=600, height=600)


head = turtle.Turtle()
head.shape("circle")
head.turtlesize(0.5)
color=random.choice(["Red","Green","orange","blue", "violet", "indigo","yellow", "purple","black"])
head.color(color)
head.direction = 0


def red():
    head.color("red")

def green():
    head.color("Green")
    
def orange():
    head.color("orange")
    
def blue():
    head.color("blue")
    
def violet():
    head.color("violet")
    
def indigo():
    head.color("indigo")

def purple():
    head.color("purple")
    
def yellow():
    head.color("yellow")

def black():
    head.color("black")
def white():
    head.color("white")

def goup():
    if head.direction != "down":
        head.direction = "up"
        move()
 
 
def godown():
    if head.direction != "up":
        head.direction = "down"
        move()
 
 
def goleft():
     if head.direction != "right":
        head.direction = "left"
        move()
    
 
def goright():
    if head.direction != "left":
        head.direction = "right"
        move()
 
def move():
    
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)
           
        
def makecircle():
    head.circle(50)      
wn.listen()
wn.onkeypress(goup, "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")
wn.onkeypress(makecircle,"c")
wn.onkey(red,"r")
wn.onkey(green,"g")
wn.onkey(violet,"v")
wn.onkey(indigo,"i")
wn.onkey(purple,"p")
wn.onkey(yellow,"y")
wn.onkey(orange,"o")
if bg=='Red':
    wn.onkey(red,'e')
if bg=='Blue':
    wn.onkey(Blue,'e')
if bg=='Violet':
    wn.onkey(violet,'e')
if bg=='Yellow':
    wn.onkey(yellow,'e')
if bg=='Black':
    wn.onkey(black,'e')
if bg=='Green':
    wn.onkey(green,'e')
wn.onkey(blue,'b')
wn.onkey(white,"t")

turtle.mainloop()



        