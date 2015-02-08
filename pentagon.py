import turtle             # Allows us to use turtles
wn = turtle.Screen()      # Creates a playground for turtles
alex = turtle.Turtle()    # Create a turtle, assign to alex
alex.shape('turtle')

for line in range(6):
    alex.forward(100)
    alex.left(360 / 6)

turtle.exitonclick()
