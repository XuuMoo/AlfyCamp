
import turtle
# loads turtle

def rectangle(edge= 100):
    turtle.color('black', 'yellow')
    turtle.begin_fill()
    for x in range(4):
        turtle.forward(edge)
        turtle.right(90)
    turtle.end_fill()
#defines how to make a body

rectangle()
#make body

def ear():
    turtle.color('black', 'yellow')
    turtle.begin_fill()
    turtle.circle(35)
    turtle.end_fill()
    turtle.color('black', 'purple')
    turtle.begin_fill()
    turtle.circle(25)
    turtle.end_fill()
#defines how to make an ear

ear()
turtle.forward(100)
ear()
#make ears

turtle.penup()
turtle.setpos((20, -35))
turtle.pendown()
turtle.color('black', 'black')
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()
turtle.color('black', 'white')
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()
turtle.penup()
#first eye
turtle.forward(60)
turtle.pendown()
turtle.color('black', 'black')
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()
turtle.color('black', 'white')
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()
turtle.penup()
#second eye

turtle.setpos((50, -45))
turtle.pendown()
turtle.color('black', 'purple')
turtle.begin_fill()
turtle.right(120)
turtle.forward(20)
turtle.left(120)
turtle.forward(20)
turtle.left(120)
turtle.forward(20)
turtle.end_fill()
turtle.penup()
#nose

turtle.setpos(25, -70)
turtle.left(155)
turtle.pendown()
turtle.pensize(3)
turtle.circle(25, 180)
#mouth

turtle.hideturtle()

turtle.exitonclick()
#keeps window open until click