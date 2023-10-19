import turtle
window = turtle.Screen()

stanley = turtle.Turtle()
stanley.speed(0)

shapes = int(input('How many shapes would you like to draw?'))
for shape in range(4, shapes+4): #shape = 5
    for number in range(shape): #shape = 5
        stanley.forward(50)
        stanley.right(360/shape)



window.exitonclick()
