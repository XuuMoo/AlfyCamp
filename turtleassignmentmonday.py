
import turtle
# loads turtle

def triangle(edge= 100):
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)
    turtle.right(60)
#defines how to make a triangle

for x in range(6):
    triangle()
#repeats 6 times

turtle.exitonclick()
#keeps window open until click