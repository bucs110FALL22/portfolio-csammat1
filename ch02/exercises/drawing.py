import turtle
my_turtle = turtle.Turtle()
my_window = turtle.Screen()
my_turtle.shape('turtle')
my_turtle.color('red')
sides = input('How many sides: ')
angle = 360 / int(sides)
for i in range (int(sides)):
  my_turtle.forward(50)
  my_turtle.left(angle)
my_window.exitonclick()