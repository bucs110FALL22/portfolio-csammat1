import turtle
import random
my_turtle = turtle.Turtle()
turtle.colormode(255)
my_turtle.shape('turtle')
my_turtle.color('purple')
for i in range (0,4):
  my_turtle.forward(50)
  my_turtle.right(90)
my_turtle.color('red')
my_turtle.forward(100)
my_turtle.left(90)
for i in range (0,3):
  my_turtle.forward(150)
  my_turtle.left(90)
my_turtle.forward(50)
my_turtle.up()
my_turtle.left(90)
my_turtle.forward(50)
my_turtle.down()
for i in range (0,4):
  random_number1 = random.randint(0,255)
  random_number2 = random.randint(0,255)
  random_number3 = random.randint(0,255)
  my_turtle.color((random_number1,random_number2,random_number3))
  my_turtle.forward(50)
  my_turtle.right(90)
  
  my_turtle.color((random_number1,random_number2,random_number3))
turtle.exitonclick()