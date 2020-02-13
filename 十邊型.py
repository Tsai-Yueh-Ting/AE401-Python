import turtle
import time
T=turtle.Turtle()
T.color('purple')
T.shape('turtle')
canvas=turtle.Screen()
canvas.title('十邊型')
canvas.bgcolor('violet')
for i in range(10):
    T.forward(50)
    T.left(36)
    time.sleep(2)
turtle.done()