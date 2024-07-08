import random
import turtle


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

# ====================== DO NOT EDIT THE CODE ABOVE ===========================


if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # Make a new turtle
    jturtle = turtle.Turtle()
    # This code sets our shape to a turtle
    jturtle.shape('turtle')
    # Set your turtle's speed (0=fastest, 1=slowest, 10=faster)
    jturtle.speed(0)
    # Set your turtle's color using .color('green')
    jturtle.color('green')
    # Use a loop to repeat a the code below 50 times
    for i in range(50):
        jturtle.color(get_random_color())
        jturtle.forward(5*i)
        jturtle.right(360/7)
        jturtle.width(i)
        # Set the turtle color to a random color

        # Move the turtle (5*i) pixels. 'i' is the loop variable
        
        # Turn the turtle (360/7) degrees to the right
         
        # Change the turtle width to 'i' (the loop variable)
        
        # Check the pattern against the picture in the recipe. If it matches, you are done!
    
# ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
