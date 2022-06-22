import turtle


"""Main window"""
win_wid = 760
win_heig = 540
win = turtle.Screen()
win.title("PingPong")
win.bgcolor("aquamarine3")
win.setup(width=win_wid, height=win_heig)
win.tracer(0)


"""Rackets"""
rack_pos = win_wid/2 - 40

racket_l = turtle.Turtle()
racket_l.speed(0)
racket_l.shape("square")
racket_l.color("black")
racket_l.shapesize(stretch_len=1, stretch_wid=5)
racket_l.penup()
racket_l.goto(-1*rack_pos, 0)


racket_r = turtle.Turtle()
racket_r.speed(0)
racket_r.shape("square")
racket_r.color("black")
racket_r.shapesize(stretch_len=1, stretch_wid=5)
racket_r.penup()
racket_r.goto(rack_pos, 0)


"""Ball"""
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("bisque2")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1
speed_run = 0.5


"""Score"""
player_1 = 0
player_2 = 0


score1 = turtle.Turtle()
score1.speed(0)
score1.shape("square")
score1.color("brown1")
score1.penup()
score1.hideturtle()
score1.goto(-200, 200)


score2 = turtle.Turtle()
score2.speed(0)
score2.shape("square")
score2.color("brown1")
score2.penup()
score2.hideturtle()
score2.goto(200, 200)


while True:
    win.update()

    """Move the ball"""
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.xcor() > 0:
        racket_r.sety(ball.ycor())
    if ball.xcor() < 0:
        racket_l.sety(ball.ycor())

    if ball.ycor() > win_heig/2-10:
        ball.sety(win_heig/2-10)
        ball.dy *= -1

    if ball.ycor() < -(win_heig/2-10):
        ball.sety(-(win_heig / 2 - 10))
        ball.dy *= -1


    if (ball.xcor() > rack_pos-10) and (ball.ycor() < racket_r.ycor() + 50) and (ball.ycor() > racket_r.ycor() - 50):
        ball.setx(rack_pos-10)
        ball.dx += speed_run
        ball.dy += speed_run
        ball.dx *= -1

    if (ball.xcor() < -(rack_pos-10)) and (ball.ycor() < racket_l.ycor() + 50) and (ball.ycor() > racket_l.ycor() - 50):
        ball.setx(-(rack_pos-10))
        ball.dx += speed_run
        ball.dy += speed_run
        ball.dx *= -1
