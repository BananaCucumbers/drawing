import turtle             # Allows us to use turtles
wn = turtle.Screen()      # Creates a playground for turtles
alex = turtle.Turtle()    # Create a turtle, assign to alex

alex.forward(200)          # Tell alex to move forward by 50 units
alex.left(90)             # Tell alex to turn by 90 degrees
alex.shape('turtle')
alex.forward(200)          # Complete the second side of a rectangle
alex.left(90)
alex.forward(200)
alex.left(90)
alex.forward(200)

turtle.exitonclick()
