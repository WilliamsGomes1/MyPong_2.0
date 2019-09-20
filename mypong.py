# Jucimar Jr 2019
# pong em turtle python https://docs.python.org/3.3/library/turtle.html
# baseado em http://christianthompson.com/node/51
# fonte DS-Digital https://www.dafont.com/pt/ds-digital.font
# som pontuação https://freesound.org/people/Kodack/sounds/258020/

import turtle
import os
import sys

# modos de jogo player vs player / player vs bot / bot vs bot
player_mode = sys.argv[1]  # "-2" "-1" "-0"

# desenhar tela
screen = turtle.Screen()
screen.title("My Pong")
screen.bgcolor("#377352")
screen.setup(width=800, height=600)
screen.tracer(0)

# desenhar raquete 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("black", "#5ca3ff")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)

# desenhar raquete 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("black", "#ff6161")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)

# desenhar bola
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("#e8971e")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# pontuação
score_1 = 0
score_2 = 0

# head-up display da pontuação
board_1 = turtle.Turtle()
board_1.speed(0)
board_1.shape("square")
board_1.color("#5ca3ff")
board_1.penup()
board_1.hideturtle()
board_1.goto(-100, 250)
board_1.write("0", align="center", font=("DS-Digital", 35, "normal"))

board_2 = turtle.Turtle()
board_2.speed(0)
board_2.shape("square")
board_2.color("#ff6161")
board_2.penup()
board_2.hideturtle()
board_2.goto(100, 250)
board_2.write("0", align="center", font=("DS-Digital", 35, "normal"))


# tracejados do centro
dashed = turtle.Turtle()
dashed.color("white")
dashed.penup()
dashed.hideturtle()
axis_y = 0
while axis_y >= -700:
    dashed.goto(0, 275+axis_y)
    dashed.write("|", align="center", font=("DS-Digital", 15, "bold"))
    axis_y -= 30

# linhas da quadra
line1 = turtle.Turtle()
line1.penup()
line1.setpos(-405, 245)
line1.color("white")
line1.pendown()
line1.setpos(405, 245)

line2 = turtle.Turtle()
line2.penup()
line2.setpos(-405, -245)
line2.color("white")
line2.pendown()
line2.setpos(405, -245)

line3 = turtle.Turtle()
line3.penup()
line3.setpos(-250, -245)
line3.color("white")
line3.pendown()
line3.setpos(-250, 245)
line3.hideturtle()

line4 = turtle.Turtle()
line4.penup()
line4.setpos(250, -245)
line4.color("white")
line4.pendown()
line4.setpos(250, 245)
line4.hideturtle()

line5 = turtle.Turtle()
line5.penup()
line5.setpos(250, 0)
line5.color("white")
line5.pendown()
line5.setpos(-250, 0)
line5.hideturtle()


# mover raquete 1
def paddle_1_up():
    y = paddle_1.ycor()
    if y < 250:
        y += 20
    else:
        y = 250
    paddle_1.sety(y)


def paddle_1_down():
    y = paddle_1.ycor()
    if y > -250:
        y += -20
    else:
        y = -250
    paddle_1.sety(y)


def paddle_2_up():
    y = paddle_2.ycor()
    if y < 250:
        y += 20
    else:
        y = 250
    paddle_2.sety(y)


def paddle_2_down():
    y = paddle_2.ycor()
    if y > -250:
        y += -20
    else:
        y = -250
    paddle_2.sety(y)


# mapeando as teclas
screen.listen()
if player_mode == '-2' or player_mode == '-1':
    screen.onkeypress(paddle_1_up, "w")
    screen.onkeypress(paddle_1_down, "s")
if player_mode == '-2':
    screen.onkeypress(paddle_2_up, "Up")
    screen.onkeypress(paddle_2_down, "Down")

while True:
    screen.update()

    # movimentação da bola
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # colisão com parede superior
    if ball.ycor() > 290:
        os.system("afplay bounce.wav&")
        ball.sety(290)
        ball.dy *= -1

    # colisão com parede inferior
    if ball.ycor() < -280:
        os.system("afplay bounce.wav&")
        ball.sety(-280)
        ball.dy *= -1

    # colisão com parede esquerda
    if ball.xcor() < -390:
        score_2 += 1
        board_2.clear()
        board_2.write(score_2, align="center", font=("DS-Digital", 35, "normal"))
        os.system("afplay 258020__kodack__arcade-bleep-sound.wav&")
        ball.goto(0, 0)
        ball.dx *= -1

    # colisão com parede direita
    if ball.xcor() > 390:
        score_1 += 1
        board_1.clear()
        board_1.write(score_1, align="center", font=("DS-Digital", 35, "normal"))
        os.system("afplay 258020__kodack__arcade-bleep-sound.wav&")
        ball.goto(0, 0)
        ball.dx *= -1

    # colisão com raquete 1
    if ball.xcor() < -330 and ball.ycor() < paddle_1.ycor() + 50 and ball.ycor() > paddle_1.ycor() - 50:
        ball.dx *= -1
        os.system("afplay bounce.wav&")

    # colisão com raquete 2
    if ball.xcor() > 330 and ball.ycor() < paddle_2.ycor() + 50 and ball.ycor() > paddle_2.ycor() - 50:
        ball.dx *= -1
        os.system("afplay bounce.wav&")

    # raquetes em modo de jogo
    if player_mode == '-1' or player_mode == '-0':
        paddle_2.sety(ball.ycor())
    if player_mode == '-0':
        paddle_1.sety(ball.ycor())
