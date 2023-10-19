import turtle
import random

top = 340
bottom = -340
left = -340
right = 340

balls = []
colors = set()
x_speeds = set()
y_speeds = set()
directions = (1, -1)

def main_method():
    number_of_balls = input('How many balls would you like to bounce?')
    instantiate_speeds()
    colors_list = get_colors_from_user()
    createBalls(number_of_balls, colors_list)
    move_balls()

def instantiate_speeds():
    for x in range(5):
        x_speeds.add(random.randint(2, 6))
        y_speeds.add(random.randint(2, 6))

def get_colors_from_user():
    user_input = input("Which colors would you like the balls to be? "
                       "Enter colors or 'start' to begin the program.")
    while user_input != 'start':
        colors.add(user_input)
        user_input = input("Which colors would you like the balls to be? "
                           "Enter colors or 'start' to begin the program.")
    return list(colors)

def createBalls(number_of_balls, colors_list):
    x_speeds_list = list(x_speeds)
    y_speeds_list = list(y_speeds)

    for i in range(int(number_of_balls)):
        ball_info = {}
        ball = turtle.Turtle()
        ball.shape("circle")
        ball.penup()
        index = i%len(colors_list)
        ball.color(colors_list[index])
        ball_info.update({'ball': ball})
        ball_info.update({'x direction': directions[random.randint(0, 1)]})
        ball_info.update({'y direction': directions[random.randint(0, 1)]})
        ball_info.update({'x speed': x_speeds_list[i%len(x_speeds_list)]})
        ball_info.update({'y speed': y_speeds_list[i%len(y_speeds_list)]})
        balls.append(ball_info)

def move_balls():
    while True:
        for ball_info in balls:
            x = ball_info['ball'].xcor()
            if x > right or x < left:
                ball_info['x direction'] = ball_info['x direction'] * -1

            y = ball_info['ball'].ycor()
            if y > top or y < bottom:
                ball_info['y direction'] = ball_info['y direction'] * -1
            ball_info['ball'].setpos(x + ball_info['x speed'] * ball_info['x direction'], y + ball_info['y speed'] * ball_info['y direction'])

main_method()