import turtle
import winsound

tela = turtle.Screen()
tela.title("Pong em Python")
tela.bgcolor("black")
tela.setup(width=800, height=600)
tela.tracer(0)

# Score, pontuação
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #mexer aqui
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #mexer aqui
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball, Bola
bola = turtle.Turtle()
bola.speed(0) #mexer aqui
bola.shape("circle")
bola.color("white")
bola.penup()
bola.goto(0, 0)
bola.dx = 0.1
bola.dy = 0.1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player I: 0 Player II: 0", align = "center", font = ("Courier", 20, "italic"))

# Função para mover os paddles
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    x = paddle_a.ycor()
    x -= 20
    paddle_a.sety(x)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    x = paddle_b.ycor()
    x -= 20
    paddle_b.sety(x)


# Keyboard binding, salvando as teclas para mover
tela.listen()
tela.onkeypress(paddle_a_up, "w")
tela.onkeypress(paddle_a_down, "s")
tela.onkeypress(paddle_b_up, "Up")
tela.onkeypress(paddle_b_down, "Down")

#Main game loop
while True:
    tela.update()

    #Move the ball, mover a bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    # Bordas, border checking
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1
        winsound.Beep(600, 75)


    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1
        winsound.Beep(600, 75)

    if bola.xcor() < -390:
        bola.goto(0, 0)
        bola.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player I: {} Player II: {}".format(score_a, score_b), align = "center", font = ("Courier", 20, "italic"))

    if bola.xcor() > 390:
        bola.goto(0, 0)
        bola.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player I: {} Player II: {}".format(score_a, score_b), align = "center", font = ("Courier", 20, "italic"))


    #Paddle and ball colisions, fisica pra bola e pro paddle
    if bola.xcor() > 340 and bola.xcor() < 350 and (bola.ycor() < paddle_b.ycor() + 50 and bola.ycor() > paddle_b.ycor() -40):
        bola.setx(340)
        bola.dx *= -1

    if bola.xcor() < -340 and bola.xcor() > -350 and (bola.ycor() < paddle_a.ycor() + 50 and bola.ycor() > paddle_a.ycor() -40):
        bola.setx(-340)
        bola.dx *= -1