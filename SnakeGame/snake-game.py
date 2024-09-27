import turtle
import time
import random

win = turtle.Screen()
win.title("Snake Game")
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("red")
head.penup()
head.goto(0, 100)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.penup()
food.goto(0, 0)
food.shapesize(0.80, 0.80)

speed = 0.125

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
        
def goUp():
    if head.direction != "down":
        head.direction = "up"
def goDown():
    if head.direction != "up":
        head.direction = "down"
def goRight():
    if head.direction != "left":
        head.direction = "right"
def goLeft():
    if head.direction != "right":
        head.direction = "left"
        
win.listen()
win.onkey(goUp, "Up")
win.onkey(goDown, "Down")
win.onkey(goRight, "Right")
win.onkey(goLeft, "Left")



while True:
    win.update()
    move()
    time.sleep(speed)
    
    if head.distance(food) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        food.goto(x, y)