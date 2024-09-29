import turtle
import time
import random

#Screen Frame
win = turtle.Screen()
win.title("Snake Game")
win.bgcolor("black")
win.setup(600, 600)
win.tracer(0)

#Snake Head
head = turtle.Turtle()  
head.speed(0)
head.shape("square")
head.color("red")
head.penup()
head.goto(0, 0)
head.direction = "stop"

#Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.penup()
food.goto(0, 100)
food.shapesize(0.80, 0.80)


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
        
tails = []
score = 0
maxScore = 0           
def eat():
    global score, maxScore
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)
        
        #Snake Tail
        tail = turtle.Turtle()
        tail.speed(0)
        tail.shape("square")
        tail.color("red")
        tail.penup()
        tails.append(tail)
        
        score += 5
        if score > maxScore:
            maxScore = score
        win.title(f"Score: {score},  Max score: {maxScore}")

    for i in range(len(tails)-1, 0, -1):
        x = tails[i-1].xcor()
        y = tails[i-1].ycor()
        tails[i].goto(x,y)
        
    if len(tails) > 0:
        x = head.xcor()
        y = head.ycor()
        tails[0].goto(x,y)
        
win.listen()
win.onkey(goUp, "Up")
win.onkey(goDown, "Down")
win.onkey(goRight, "Right")
win.onkey(goLeft, "Left")

while True:
    win.update()
    eat()
    move()
    time.sleep(0.1)
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        for tail in tails:
            tail.goto(1000, 1000)
        
        tails.clear()
        score = 0
        win.title(f"Score: {score},  Max score: {maxScore}")