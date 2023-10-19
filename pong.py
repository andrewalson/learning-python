import random
import turtle
import time
window = turtle.Screen()

width = 300
height = 300

turtle.screensize(width, height, 'light blue')
window.register_shape('pongpaddle.gif')

def left_player2():
    player2.setx(player2.xcor() - increment)

def right_player2():
    player2.setx(player2.xcor() + increment)

def right_player1():
    player1.setx(player1.xcor() + increment)

def left_player1():
    player1.setx(player1.xcor() - increment)

def player_setup():
    player1.shape('pongpaddle.gif')
    player2.shape('pongpaddle.gif')
    player1.penup()
    player2.penup()
    player1.sety(height - 20)
    player2.sety((height - 20) * -1)

    window.onkey(left_player1, 'Left')
    window.onkey(right_player1, 'Right')
    window.onkey(left_player2, 'a')
    window.onkey(right_player2, 'd')
    window.listen()

def ball_setup():
    ball_info.update({'x speed': random.randint(1, 28)})
    ball_info.update({'y speed': random.randint(1, 28)})
    ball_info.update({'x direction': random.choice(direction)})
    ball_info.update({'y direction': random.choice(direction)})
    ball_info.update({'ball': ball})
    ball.penup()

def move_ball():
    ball_info['ball'].setpos(ball_info['ball'].xcor() + ball_info['x speed'] * ball_info['x direction'],
                            ball_info['ball'].ycor() + ball_info['y speed'] * ball_info['y direction'])

def reset_ball():
    ball_info['ball'].reset()
    ball_setup()
    ball.color('red')
    time.sleep(3)

def detect_collision():
    x = ball_info['ball'].xcor()
    if x > width or x < -width:
        ball_info['x direction'] = ball_info['x direction'] * -1

    y = ball_info['ball'].ycor()

    paddle1x = player1.xcor()
    paddle2x = player2.xcor()
    if y > height-52:
        if x <= (paddle1x + 103) and x >= (paddle1x - 103):
            ball_info['y direction'] = ball_info['y direction'] * -1
        else:
            global player1_score
            player1_score_display.clear()
            player1_score = player1_score -1
            score_change()
            reset_ball()

    elif y < -height+52:
        if x <= (paddle2x + 103) and x >= (paddle2x - 103):
            ball_info['y direction'] = ball_info['y direction'] * -1
        else:
            global player2_score
            player2_score_display.clear()
            player2_score = player2_score -1
            score_change()
            reset_ball()

def start_game():
    window.onkey(None, 'space')
    instruction.clear()
    while player1_score > 0 and player2_score > 0:
        move_ball()
        detect_collision()

def instructions():
    instruction.penup()
    instruction.hideturtle()
    instruction.color('magenta')
    instruction.write('Press spacebar to begin', False, 'center', ('comic sans', 50, 'bold'))
    window.onkey(start_game, 'space')

def scoreboard():
    player1_score_display.penup()
    player2_score_display.penup()
    player1_score_display.hideturtle()
    player2_score_display.hideturtle()
    player1_score_display.color('brown')
    player2_score_display.color('brown')
    player1_score_display.setpos(250, 250)
    player2_score_display.setpos(-250, -250)

def score_change():
    player1_score_display.write(player1_score, False, 'center', ('comic sans', 35 , 'bold'))
    player2_score_display.write(player2_score, False, 'center', ('comic sans', 35 , 'bold'))

def main_method():
    player_setup()
    ball_setup()
    instructions()
    scoreboard()
    score_change()

player1 = turtle.Turtle()
player2 = turtle.Turtle()
increment = 13
ball_info = {}
direction = (1, 1)
player1_score = 3
player2_score = 3
instruction = turtle.Turtle()
player1_score_display = turtle.Turtle()
player2_score_display = turtle.Turtle()
ball = turtle.Turtle()
ball.shape('circle')
ball.color('red')

main_method()
window.exitonclick()