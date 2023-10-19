import turtle
window = turtle.Screen()

stanley = turtle.Turtle()
stanley.speed(0)

#sides = int(input('How many sides would you like the shape to have? Or type 0 to stop.'))
sides = None
while sides != 0:
    sides = int(input('How many sides would you like the shape to have? Or type 0 to stop.'))
    for number in range(sides): 
        stanley.forward(50)
        stanley.right(360/sides)

print('exited')


window.exitonclick()
