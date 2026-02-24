# from turtle import Screen, Turtle
import turtle as t

timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("red")


for _ in range(4):
    for i in range(100):
        if i % 5 == 0:
            timmy.penup()
        else:
            timmy.pendown()
        timmy.forward(1)
    timmy.right(90)


screen = t.Screen()

screen.exitonclick()