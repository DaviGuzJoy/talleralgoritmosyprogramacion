#initializing
import turtle
an=turtle.Screen()
a=turtle.Turtle()

#setting up pen and page
an.bgcolor("black")
a.color("red")
a.shape("arrow")
a.pensize(10)

#moving pen left to start
a.penup()
a.left(90)
a.bk(260)
a.pendown()
#wriring: D
a.pendown()
a.right(90)
a.circle(80,180)
a.left(90)
a.fd(160)
#espacio
a.penup()
a.left(90)
a.fd(120)
a.pendown()
#letra a
a.color("green")
a.right(106)
a.bk(155)
a.left(30)
a.fd(155)
a.bk(60)
a.right(106)
a.fd(45)
a.bk(45)
a.left(106)
a.fd(60)
#espacio
a.penup()
a.left(120)
a.fd(120)
a.pendown()
#letra v
a.color("pink")
a.right(108)
a.forward(150)
a.left(135)
a.forward(150)
#espacio
a.penup()
a.left(120)
a.fd(-45)
a.pendown()
#letra i
a.color("aqua")
a.fd(15)
a.left(90)
a.fd(150)
a.right(90)
a.fd(15)
a.bk(30)
a.fd(15)
a.right(90)
a.fd(150)
a.right(90)
a.bk(15)
#espacio
a.penup()
a.right(-130)
a.fd(-200)
a.pendown()
#letra D
a.pensize(10)
a.pencolor("purple")
a.left(100)
a.forward(70)
a.right(120)
a.forward(50)
a.right(60)
a.forward(30)
a.right(90)
a.forward(45)
a.left(90)
a.forward(40)

#figurita
a.pensize(2)
a.speed(5)
a.pencolor("blue")
sizee= 5
for i in range(sizee*100):
    a.forward(i)
    a.left(91)
turtle.done()




