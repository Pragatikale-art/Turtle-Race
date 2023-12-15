import turtle
import random
is_race_on = False
all_turtle = []

screen = turtle.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(prompt="Please enter your turtle you think will win", title="Make your bet")
colors = ["red", "green", "brown", "orange", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
for turtle_index in range(6):
    new_turtle = turtle.Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y= y_position[turtle_index])
    all_turtle.append(new_turtle)
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor()> 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color== user_bet:
                print(f"You won!, the {winning_color} turtle is the winner! ")
            else:
                print(f"You lost!, the {winning_color} turtle is the winner!")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()