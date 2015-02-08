import turtle             # Allows us to use turtles
wn = turtle.Screen()      # Creates a playground for turtles
alex = turtle.Turtle()    # Create a turtle, assign to alex
alex.shape('turtle')

for line in range(4):
    alex.forward(200)
    alex.left(90)

turtle.exitonclick()
