import turtle
screen = turtle.Screen()
screen.bgcolor("white")
heart = turtle.Turtle()
heart.speed(3)
heart.color("red")
heart.shape("classic")
def draw_heart():
    heart.begin_fill()
    heart.left(140)
    heart.forward(180)
    heart.circle(-90, 200)

    heart.left(120)
    heart.circle(-90, 200)
    heart.forward(180)
    heart.end_fill()
def write_text():
    heart.penup()
    heart.goto(-55, 120)
    heart.color("white")
    heart.write("akka", font=("Georgia", 24, "bold"))
    heart.hideturtle()
draw_heart()
write_text()
turtle.done()