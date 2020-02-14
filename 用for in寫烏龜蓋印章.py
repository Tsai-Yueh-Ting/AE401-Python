import turtle
T=turtle.Turtle()
T.color('purple')
T.shape('turtle')
canvas=turtle.Screen()
canvas.title('烏龜繞圈的圖')
canvas.bgcolor('violet')
count=0
T.penup()
for i in range(0,300):
    T.stamp()
    T.forward(count)
    T.left(20)
    count+=0.5
turtle.done()