import turtle
import random
my_turtle = turtle.Turtle()
my_window = turtle.Screen()
my_turtle.shape('turtle')
my_turtle.color('green')
coin = ['heads', 'tails']
while -150 < my_turtle.pos()[1] < 150 and -300 < my_turtle.pos()[0] < 300: #couldn't figure out how to calculate the height and width. These values I determined by eye.
  dir = random.randint(0,1)
  if dir == 0:
    my_turtle.left(90)
  if dir ==1:
    my_turtle.right(90)
  my_turtle.forward(50)
turtle.exitonclick()