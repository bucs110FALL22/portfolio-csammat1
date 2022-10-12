import turtle

def drawEqShape(turtle = None, num_sides=0, side_length=0):
  angle = 360/num_sides
  for i in range(0,num_sides):
    turtle.forward(side_length)
    turtle.left(angle)

leo = turtle.Turtle()
my_window = turtle.Screen()
leo.shape("turtle")
leo.color('green')
num_sides = int(input('How many sides:'))
side_length = int(input('How long is each side:'))
drawEqShape(leo, num_sides, side_length) #not sure why it creates a new turtle object at the origin, it does not move though.
my_window.exitonclick()