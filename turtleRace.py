import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?: ")
print(user_bet)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles = []

x = -230
y = -100
for turtle_index in range(0,6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])

    new_turtle.goto(x=x, y=y)
    y += 40
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won. {winning_color} won.")
            else:
                print(f"You've lost. {winning_color} won.")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()

















