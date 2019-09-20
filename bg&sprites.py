import turtle
import os

# desenhar tela
screen.bgcolor("#377352")

# desenhar raquete 1
paddle_1.color("black", "#5ca3ff")

# desenhar raquete 2
paddle_2.color("black", "#ff6161")

# desenhar bola
ball.shape("circle")
ball.color("#e8971e")

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


while True:
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
