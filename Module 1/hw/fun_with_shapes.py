import turtle

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("lightblue")  # Setting background color
t = turtle.Turtle()
t.speed(3)
t.width(2)

def draw_shape(sides, length, color, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    
    # Calculate angle: 360 / number of sides
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.left(angle)
    
    t.end_fill()

# 1. Equilateral Triangle (3 sides)
draw_shape(3, 100, "yellow", -200, 0)

# 2. Rectangle (Special case: 2 long sides, 2 short)
t.penup()
t.goto(-50, 0)
t.pendown()
t.fillcolor("orange")
t.begin_fill()
for _ in range(2):
    t.forward(120)
    t.left(90)
    t.forward(70)
    t.left(90)
t.end_fill()

# 3. Hexagon (6 sides)
draw_shape(6, 60, "lightgreen", 150, 0)

# Hide turtle and keep window open
t.hideturtle()
screen.mainloop()
