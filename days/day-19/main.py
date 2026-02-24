# from turtle import Screen, Turtle
import turtle as t

timmy = t.Turtle()


def move_forwards():
    timmy.forward(10)

def move_backwards():
    timmy.backward(10)

def turn_left():
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)

def turn_right():
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)

def clear_screen():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen = t.Screen()

screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()