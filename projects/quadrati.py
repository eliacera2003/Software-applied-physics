import turtle

t = turtle.Turtle()
t.speed(0)

colors = ["red", "blue", "green", "purple", "orange"]

for i in range(36):
    t.pencolor(colors[i % len(colors)])

    for j in range(4):
        t.forward(150)
        t.right(90)

    t.right(10)

turtle.done()