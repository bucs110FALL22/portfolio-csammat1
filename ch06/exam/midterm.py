import turtle
def main():
  
  length = 10
  my_window = turtle.Screen()
  my_turtle = turtle.Turtle()
  my_turtle.shape('turtle')
  
  
  number = draw_pixel(my_turtle, 'black', 8) #row 1
  next_row(my_turtle, x_pos = -length)
  
  number += draw_pixel(my_turtle, 'black', 10) #row 2
  next_row(my_turtle, x_pos = 2*-length)
  
  number += draw_pixel(my_turtle, 'black', 4) #row 3
  number += draw_pixel(my_turtle, 'white', 6)
  number += draw_pixel(my_turtle, 'black', 1)
  next_row(my_turtle, x_pos = -3*length)
  
  number += draw_pixel(my_turtle, 'black', 4) # row 4
  number += draw_pixel(my_turtle, 'white', 8)
  number += draw_pixel(my_turtle, 'black', 1)
  next_row(my_turtle, x_pos = -3*length)
  
  number += draw_pixel(my_turtle, 'black', 4) #row 5
  number += draw_pixel(my_turtle, 'white', 1)
  number += draw_pixel(my_turtle, 'black', 2)
  number += draw_pixel(my_turtle, 'white', 4)
  number += draw_pixel(my_turtle, 'black', 2)
  next_row(my_turtle, x_pos =-3*length)
  
  number += draw_pixel(my_turtle, 'black', 3) #row 6
  number += draw_pixel(my_turtle, 'white', 1)
  number += draw_pixel(my_turtle, 'black', 2)
  number += draw_pixel(my_turtle, 'white', 1)
  number += draw_pixel(my_turtle, 'black', 1)
  number += draw_pixel(my_turtle, 'white', 2)
  number += draw_pixel(my_turtle, 'black', 2)
  number += draw_pixel(my_turtle, 'white', 1)
  number += draw_pixel(my_turtle, 'black', 1)
  next_row(my_turtle, x_pos =-3*length)

  number += draw_pixel(my_turtle, 'black', 3) #row 7
  number += draw_pixel(my_turtle, 'white', 1)
  number += draw_pixel(my_turtle, 'black', 4)
  number += draw_pixel(my_turtle, 'white', 2)
  number += draw_pixel(my_turtle, 'black', 4)
  next_row(my_turtle, x_pos =-3*length)

  number += draw_pixel(my_turtle, 'black', 3) #row 8
  number += draw_pixel(my_turtle, 'white', 2)
  number += draw_pixel(my_turtle, 'black', 2)
  number += draw_pixel(my_turtle, 'white', 2)
  number += draw_pixel(my_turtle, 'yellow', 2)
  number += draw_pixel(my_turtle, 'black', 2)
  
  next_row(my_turtle, x_pos =-3*length)
  number += draw_pixel(my_turtle, 'black', 3)#row 9
  number += draw_pixel(my_turtle, 'white', 5)
  number += draw_pixel(my_turtle, 'yellow', 5)
  next_row(my_turtle, x_pos =-3*length)

  number += draw_pixel(my_turtle, 'black', 4)#row 10
  number += draw_pixel(my_turtle, 'white', 5)
  number += draw_pixel(my_turtle, 'yellow', 5)
  next_row(my_turtle, x_pos =-3*length)

  number += draw_pixel(my_turtle, 'black', 5)#row 11
  number += draw_pixel(my_turtle, 'white', 4)
  number += draw_pixel(my_turtle, 'yellow', 3)
  number += draw_pixel(my_turtle, 'black', 3)
  next_row(my_turtle, x_pos =-3*length)

  number += draw_pixel(my_turtle, 'black', 6)#row12
  number += draw_pixel(my_turtle, 'white', 6)
  number += draw_pixel(my_turtle, 'black', 4)
  next_row(my_turtle, x_pos =-3*length)

  number += draw_pixel(my_turtle, 'black', 2)#row 13
  number += draw_pixel(my_turtle, 'white', 1)
  number += draw_pixel(my_turtle, 'black', 3)
  number += draw_pixel(my_turtle, 'white', 6)
  number += draw_pixel(my_turtle, 'black', 4)
  next_row(my_turtle, x_pos =-3*length)

  number += draw_pixel(my_turtle, 'black', 2)#row 14
  number += draw_pixel(my_turtle, 'white', 2)
  number += draw_pixel(my_turtle, 'black', 2)
  number += draw_pixel(my_turtle, 'white', 6)
  number += draw_pixel(my_turtle, 'black', 1)
  number += draw_pixel(my_turtle, 'white', 1)
  number += draw_pixel(my_turtle, 'black', 2)
  next_row(my_turtle, x_pos =-2*length)

  number += draw_pixel(my_turtle, 'black', 1)#row 15
  number += draw_pixel(my_turtle, 'white', 10)
  number += draw_pixel(my_turtle, 'black', 1)
  next_row(my_turtle, x_pos =-2*length)

  number += draw_pixel(my_turtle, 'black', 2)#row 16
  number += draw_pixel(my_turtle, 'white', 8)
  number += draw_pixel(my_turtle, 'black', 1)
  next_row(my_turtle, x_pos =-length)

  number += draw_pixel(my_turtle, 'black', 10)#row 17
  next_row(my_turtle, x_pos =-length)

  number += draw_pixel(my_turtle, 'black', 1)#row18
  number += draw_pixel(my_turtle, 'orange', 3)
  number += draw_pixel(my_turtle, 'black', 2)
  number += draw_pixel(my_turtle, 'orange', 3)
  number += draw_pixel(my_turtle, 'black', 1)
  next_row(my_turtle, x_pos =-length)

  number += draw_pixel(my_turtle, 'black', 4)#row 19
  number += draw_pixel(my_turtle, 'white', 2)
  number += draw_pixel(my_turtle, 'black', 4)
  print('There are ' + str(number) + ' pixels in this drawing')
  my_window.exitonclick()
def draw_pixel(my_turtle = turtle, color = 'black', number = 1, length = 10): 
  my_turtle.color(color)
  my_turtle.begin_fill()
  for i in range(2):
    my_turtle.forward(length*number)
    my_turtle.left(90)
    my_turtle.forward(length)
    my_turtle.left(90)
  my_turtle.end_fill()
  my_turtle.forward(length*number)
  return number

def next_row(my_turtle = turtle, x_pos = 0, length = 10 ):
  my_turtle.penup()
  current_ypos = my_turtle.position()[1]
  my_turtle.goto(x_pos, current_ypos-length)
  my_turtle.pendown()
main()