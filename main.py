import turtle

def drawSquare(t, sz):
    """get turtle t to draw a square of sz side"""
    for i in range(20):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")
drawSquare(alex,50)
wn.exitonclick()
