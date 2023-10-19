import turtle
window = turtle.Screen()

stanley = turtle.Turtle()
stanley.speed(0)

#sides = int(input('How many sides would you like the shape to have? Type done to stop.'))
user_input = 0
while user_input != 'done':
    sides = int(user_input)
    for number in range(sides): 
        stanley.forward(50)
        stanley.right(360/sides)
    user_input = input('How many sides would you like the shape to have? Type done to stop.')

