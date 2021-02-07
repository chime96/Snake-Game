# Simple Snake Game
# By Tech@chime

import os
import turtle
import time
import random

wn = turtle.Screen()
wn.title("Snake Game By Tech@chime")
wn.bgcolor("green")
wn.setup(width=600,height=600)
wn.tracer(0)

delay = 0.1
score = 0
high_score = 0

# Snake Head
head = turtle.Turtle()
head.shape("square")
head.speed(0)
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

# Create segments
segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,265)
pen.write("Score:0 HighScore:0",align="center",font=("courier",24,"normal"))

# Function
# Direction of go

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"


# Movement
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x - 20)

    
    
# KeyBoard Binding
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Right")
wn.onkeypress(go_right, "Left")



# Main Game Loop
while True:
    wn.update()
    time.sleep(delay)


    # Check for a Collision with the border
    if head.xcor() > 240 or head.xcor() < -240 or head.ycor() > 240 or head.ycor() < -240:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Hide the Segments
        for segment in segments:
            segment.goto(1000,1000)

        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {} HighScore: {}".format(score,high_score),align="center",font=("courier",24,"normal"))
        





    
    # Checking for collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-245,245)
        y = random.randint(-245,245)
        food.goto(x,y)
    
        # Add a New Segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("gray")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the Delay

        delay -= 0.001

         # Add Increase Score
        score += 10

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {} HighScore: {}".format(score,high_score),align="center",font=("courier",24,"normal"))
        
    
    # Move the end of segments first in reverse order
    for index in range(len(segments) -1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    
    # Move segments 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    # Check for head collision with body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # Hide the segment
            for segment in segments:
                segment.goto(1000,1000)
            
            # Clear the segment list
            segments.clear()

wn.mainloop()
input("press any key to end")