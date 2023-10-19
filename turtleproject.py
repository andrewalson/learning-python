import turtle
import random
stanley = turtle.Turtle()

def main_program():
    selection = None
    while selection != 'q' or selection != 'quit':

        print(""""
        Welcome to Turtle! Please choose from the following options:
        Type 1 for drawing circles.
        Type 2 for drawing random lines.
        Type 3 for changing the pen color.
        Type 4 for adjusting pen size.
        Type 5 for changing the Turtle speed.
        Type 6 to clear your drawing.
        Type ‘q’ or ‘quit’ to quit the program.""")

        selection = input("Which option woulad you like?")

        if selection == "1":
            num = int(input("How many circles would you like to draw?"))
            diameter = int(input("How big in diameter would you like the circles to be?"))
            draw_circles(num, diameter)

        elif selection == "2":
            #num = input(int("How many random lines would you like?"))
            num = int(input("How many random lines would you like?"))
            draw_lines(num)

        elif selection == "3":
            print("""Choose color from the following options:
                Type 1 for Red.
                Type 2 for Green.
                Type 3 for Blue.
                Type 'q' to quit.""")
            color = input("Which color would you like?")
            if color == "1":
                stanley.pencolor("red")
            elif color == "2":
                stanley.pencolor("green")
            elif color == "3":
                stanley.pencolor("blue")
            elif color == "q":
                exit()
            else:
                print("Please choose a valid menu option.")
           # stanley.colormode()
           # stanley.pencolor()

        elif selection == "4":
            print("Adjusting pen size. Press 'c' to check the current size.")
            size = input("Then, choose your pen size on a scale of 1-10")
            if size == 'c':
                print(stanley.pensize())
            else:
                stanley.pensize(int(size))

        elif selection == "5":
            print("What speed would you like to draw at on a scale from 1-10?")
            pace = int(input("Or, press 0 for superspeed."))
            stanley.speed(pace)

        elif selection == "6":
            stanley.clear()

        elif selection == 'q' or 'quit':
            exit()
        else:
            print("Please choose a valid menu option.")

def draw_lines(num):
    for n in range(0, num):
        x = random.randint(-400, 400)
        y = random.randint(-400, 400)
        point = (x, y)
        stanley.goto(point)

def draw_circles(num, diameter):
    for cir in range(num):
        stanley.circle(diameter / 2)
        stanley.left(360 / num)

main_program()