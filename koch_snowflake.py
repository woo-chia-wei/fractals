import turtle
import re

turtle.shape('turtle')
turtle.colormode(255)
turtle.pensize(1)
turtle.pencolor(0,255,0)
turtle.fillcolor(0,0,0)
turtle.speed(50)
turtle.bgcolor(0,0,0)
turtle.hideturtle()
turtle.speed(0)

def draw_koch(n, length):
	if n == 0:
		turtle.forward(length)
	else:
		turtle.left(0)
		draw_koch(n-1, length/3)
		turtle.left(60)
		draw_koch(n-1, length/3)
		turtle.right(120)
		draw_koch(n-1, length/3)
		turtle.left(60)
		draw_koch(n-1, length/3)

def draw_koch_snowflake(n, length):
	turtle.left(120)
	draw_koch(n, length)
	turtle.right(120)
	draw_koch(n, length)
	turtle.right(120)
	draw_koch(n, length)
	turtle.left(120)

def create_koch_snowflake_shape(n, length, x, y):
	turtle.penup()
	turtle.goto(x, y)
	turtle.pendown()
	draw_koch_snowflake(n, length)
	turtle.penup()

length = 70
create_koch_snowflake_shape(n=0, length=length, x=-300, y=300)
create_koch_snowflake_shape(n=1, length=length, x=-300, y=200)
create_koch_snowflake_shape(n=2, length=length, x=-300, y=100)
create_koch_snowflake_shape(n=3, length=length, x=-300, y=0)
create_koch_snowflake_shape(n=4, length=length, x=-300, y=-100)


turtle.getscreen()._root.mainloop() 



