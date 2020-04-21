import turtle
from random import randint
import math

x = -100
y = 100
r = randint(0,1)
t = turtle.Turtle()

t.speed("fastest")
t.penup()
t.setpos(x,y)
theda = math.radians(60)
h = math.sin(theda)*10

for i in range (0,40):
  if i%2==1:
    t.penup()
    t.forward(5)
  if r ==0:
      t.penup()
      t.forward(10)
  for j in range (0,20):
    t.pendown()
    t.forward(10)
    t.penup()
    t.forward(10)
  y=y-h
  r=randint(0,1)
  t.penup()
  t.setpos(x,y)
  
y=100
x=-200
t.penup()
t.setpos(x,y)
t.right(60)

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
  
y=100
x=0
t.penup()
t.setpos(x,y)
t.right(60)

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
