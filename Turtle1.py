import turtle
import time
import random
number=random.randint(0,180)
T=turtle.Turtle()
T.color('purple')
T.shape('turtle')
canvas=turtle.Screen()
canvas.title('烏龜爬牆壁')
canvas.bgcolor('violet')
count=0
while count<40:
    T.forward(100)
    T.left(number)
    time.sleep(1)
    count+=1
turtle.done()