import turtle


window = turtle.Screen()
window.bgcolor('white')

# This code makes a new Turtle. Pick a new name for the turtle
jack_the_turtle = turtle.Turtle()

# Make your turtle's shape 'turtle', .shape('turtle')
jack_the_turtle.shape('circle')
# Set your turtle's speed using .speed(2)
jack_the_turtle.speed(2)
# Set your turtle's color using .color('green') and .pencolor('blue')
jack_the_turtle.color('green')
jack_the_turtle.pencolor('blue')
# Move your turtle forward using .forward(100)
jack_the_turtle.forward(100)
# TEST    Did your turtle move forward?

# Move your turtle left or right using .left(90) or .right(90)
jack_the_turtle.left(90)
# Now put the forward and left/right code into a for loop to repeat 4 times.
for i in range(4):
    jack_the_turtle.forward(100)
    jack_the_turtle.right(90)
# TEST    Did your turtle draw a square?

# Move your turtle to a new place on the screen using .goto(x, y)
# x=0 and y=0 is the center of the screen
jack_the_turtle.goto(200, 200)
# Have your turtle draw a circle using .circle(radius, steps=30)
# TEST    Did your turtle draw a circle?
jack_the_turtle.begin_fill()
jack_the_turtle.circle(200, steps=40)
# Add color to your shape by adding .begin_fill() before drawing the circle
# and .end_fill() below
jack_the_turtle.end_fill()
# Draw 3 more shapes with different fill colors!
jack_the_turtle.color('orange')
jack_the_turtle.begin_fill()
for i in range(4):
    jack_the_turtle.forward(100)
    jack_the_turtle.right(90)
jack_the_turtle.end_fill()
jack_the_turtle.goto(-50,-50)

jack_the_turtle.color('blue')
jack_the_turtle.begin_fill()
for i in range(4):
    jack_the_turtle.forward(100)
    jack_the_turtle.right(90)
jack_the_turtle.end_fill()
jack_the_turtle.goto(-150,-150)

jack_the_turtle.color('red')
jack_the_turtle.begin_fill()
for i in range(4):
    jack_the_turtle.forward(100)
    jack_the_turtle.right(90)
jack_the_turtle.end_fill()
jack_the_turtle.goto(-250,-250)

# ===================== DO NOT EDIT THE CODE BELOW ============================
turtle.done()
