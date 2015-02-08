import turtle             # Allows us to use turtles
wn = turtle.Screen()      # Creates a playground for turtles
alex = turtle.Turtle()    # Create a turtle, assign to alex
alex.shape('turtle')

def shape(sides, size):
    for line in range(sides):
        alex.forward(size)
        alex.left(360 / sides)

shape(12, 15)
turtle.exitonclick()
