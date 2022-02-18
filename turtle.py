import turtle
t = turtle.Turtle()
t.shape('turtle')
t.speed(0)
for i in range(6):
    for colours in ["red","blue","green","yellow","cyan","purple"]:
        t.color(colours)
        t.circle(100)
        t.left(10)
t.hideturtle()
        
