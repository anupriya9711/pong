import turtle


sc = turtle.Screen()
sc.title("pong game by anupriya")
sc.bgcolor("green")
sc.setup(width=800, height=600)
sc.tracer()

# Bar A
bar_A = turtle.Turtle()
bar_A.shape('square')
bar_A.color('black')
bar_A.shapesize(stretch_wid=5, stretch_len=1)
bar_A.penup()
bar_A.goto(-350,0)

# Bar B
bar_B = turtle.Turtle()
bar_B.shape('square')
bar_B.color('black')
bar_B.shapesize(stretch_wid=5, stretch_len=1)
bar_B.penup()
bar_B.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.shape('circle')
ball.color('pink')
ball.penup()
ball.goto(0,0)
ball_x=0.1
ball_y=0.1

# score
sboard = turtle.Turtle()
sboard.shape('square')
sboard.color('white')
sboard.penup()
sboard.hideturtle()
sboard.goto(0, 260)
sboard.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24,'normal'))

score_a = 0
score_b = 0

def bar_A_up():
    y = bar_A.ycor()
    y += 30
    bar_A.sety(y)
def bar_A_down():
    y = bar_A.ycor()
    y -= 30
    bar_A.sety(y)
def bar_B_up():
    y = bar_B.ycor()
    y += 30
    bar_B.sety(y)
def bar_B_down():
    y = bar_B.ycor()
    y -= 30
    bar_B.sety(y)

# Keyboard Bindings
sc.listen()
sc.onkeypress(bar_A_up, 'W')
sc.onkeypress(bar_A_down, 'S')
sc.onkeypress(bar_B_up, 'Up')
sc.onkeypress(bar_B_down, 'Down')

while True:
    sc.update()

    # BAll movement
    ball.setx(ball.xcor() + ball_x)
    ball.sety(ball.ycor() + ball_y)

    # Border
    if ball.ycor() > 290:
        ball.sety(290)
        ball_y *= -1
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball_y *= -1
        #score
    if ball.xcor() > 350:
        score_a += 1
        sboard.clear()
        sboard.write("Player A: {} Player B {}".format(score_a, score_b), align='center', font=('Courier', 24, 'normal'))
        ball.goto(0,0)
        ball_x *= -1
    elif ball.xcor() < -350:
        score_b += 1
        sboard.clear()
        sboard.write("Player A: {} Player B {}".format(score_a, score_b), align='center',
                     font=('Courier', 24, 'normal'))
        ball.goto(0, 0)
        ball_x *= -1


    # Collision with bars
    if ball.xcor() < -340 and ball.ycor() < bar_A.ycor() + 50 and ball.ycor() > bar_A.ycor() - 50:
        ball_x *= -1
    elif ball.xcor() > 340 and ball.ycor() < bar_B.ycor() + 50 and ball.ycor() > bar_B.ycor() - 50:
        ball_x *= -1
