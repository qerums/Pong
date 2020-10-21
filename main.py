import turtle

window = turtle.Screen()
window.title('Pong')
window.bgcolor('black')
window.setup(width=800, height=600)
window.tracer(0)



def schuif(x,y):  
  schuif = turtle.Turtle()
  schuif.speed(0)
  schuif.shape('square')
  schuif.color('yellow')
  schuif.shapesize(stretch_wid=5, stretch_len=1)
  schuif.penup()
  schuif.goto(x,y)

bal = turtle.Turtle()
bal.speed(0)
bal.shape('circle')
bal.color('white')
bal.penup()
bal.goto(0,0)
bal.dx =2
bal.dy =-2

schuif1 = schuif(-350, 0)
schuif2 = schuif(350, 0)

def schuif1_up():
  y = schuif1.ycor()
  y += 20
  schuif1.sety(y)

def schuif1_down():
  y = schuif1.ycor()
  y -= 20
  schuif1.sety(y)

def schuif2_up():
  y = schuif2.ycor()
  y += 20
  schuif2.sety(y)

def schuif2_down():
  y = schuif2.ycor()
  y -= 20
  schuif2.sety(y)

window.listen()
window.onkeypress(schuif1_up, "w")
window.onkeypress(schuif1_down, "x")
window.onkeypress(schuif2_up, "Up")
window.onkeypress(schuif2_down, "Down")

while True:
  window.update()
  bal.setx(bal.xcor() + bal.dx)
  bal.sety(bal.ycor() + bal.dy)

  if bal.ycor() > 290:
    bal.sety(290)
    bal.dx *= -1

  if bal.ycor() < -290:
    bal.sety(-290)
    bal.dx *= -1

  if bal.xcor() > 390:
    bal.sety(390)
    bal.dy *= -1

  if bal.xcor() > -390:
    bal.sety(-390)
    bal.dy *= -1
