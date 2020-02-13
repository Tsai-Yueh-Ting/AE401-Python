import turtle
T=turtle.Turtle()
T.color('purple')
T.shape('turtle')
canvas=turtle.Screen()
canvas.title('用while寫烏龜繞蝸牛殼狀走')
canvas.bgcolor('violet')
count=0
count=int(count)
while count<300:
    T.forward(count)
    T.left(5)
    count+=0.05
turtle.done()