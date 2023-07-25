#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Author: Devan Blanscett
' Program name: pong
' Program Description: simple pong program that lets us play with two people following along 
'							  with video "learn python by building five games - full course" by 
'							  "freeCodeCamp.org", URL: https://www.youtube.com/watch?v=XGf2GcyHPhc
'
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#code body here

import turtle #basic graphics module

win = turtle.Screen() #window
win.title("Pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0) #requires the window to manually be updated

#paddle A
paddle_a = turtle.Turtle()#basic tutle object
paddle_a.speed(0)#max speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()#by default turtles draw lines as they move, this stops that
paddle_a.goto(-350,0)

#paddle B
paddle_b = turtle.Turtle()#basic tutle object
paddle_b.speed(0)#max speed
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()#by default turtles draw lines as they move, this stops that
paddle_b.goto(350,0)

#Ball
ball = turtle.Turtle()#basic tutle object
ball.speed(0)#max speed
ball.shape("square")
ball.color("white")
ball.penup()#by default turtles draw lines as they move, this stops that
ball.goto(0,0)
ball.dx = 2
ball.dy = 2


def paddle_a_up():
	y = paddle_a.ycor()
	y += 20
	paddle_a.sety(y)

def paddle_a_down():
	y = paddle_a.ycor()
	y -= 20
	paddle_a.sety(y)

def paddle_b_up():
	y = paddle_b.ycor()
	y += 20
	paddle_b.sety(y)

def paddle_b_down():
	y = paddle_b.ycor()
	y -= 20
	paddle_b.sety(y)

#keyboard binding
win.listen()
win.onkeypress(paddle_a_up,"w")#not a function call, binding the function to the key
win.onkeypress(paddle_a_down,"s")
win.onkeypress(paddle_b_up,"Up")#not a function call, binding the function to the key
win.onkeypress(paddle_b_down,"Down")




#main game loop
while True:
	win.update()

	#move the ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)
	
	#border checking
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1
	if ball.ycor() < -290:
		ball.sety(-290)
		ball.dy *= -1
	if ball.xcor() > 390:
		ball.goto(0, 0)
		ball.dx *= -1
	if ball.xcor() < -390:
		ball.goto(0, 0)
		ball.dx *= -1

	#paddle bounce
	if ball.xcor() + 10 >= paddle_b.xcor() and ball.xcor() < paddle_b.xcor():
		if paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50:
			ball.setx(340)
			ball.dx *= -1

	if ball.xcor() - 10 <= paddle_a.xcor() and ball.xcor() > paddle_a.xcor():
		if paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50:
			ball.setx(-340)
			ball.dx *= -1
