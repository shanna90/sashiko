import turtle
from random import randint

x = -100
y = 100
r = randint(0,1)
t = turtle.Turtle()

t.speed("fastest")
t.penup()
t.setpos(x,y)

for i in range (0,40):
  if r ==0:
      t.penup()
      t.forward(10)
  for j in range (0,20):
    t.pendown()
    t.forward(10)
    t.penup()
    t.forward(10)
  y=y-10
  r=randint(0,1)
  t.penup()
  t.setpos(x,y)
  
y=100
t.penup()
t.setpos(x,y)
t.right(90)

for i in range (0,40):
  if r ==0:
      t.penup()
      t.forward(10)
  for j in range (0,20):
    t.pendown()
    t.forward(10)
    t.penup()
    t.forward(10)
  x=x+10
  r=randint(0,1)
  t.penup()
  t.setpos(x,y)
