import turtle #1. import modules
import random
import time
import pygame
import math

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
mic_random_distance = random.randrange(1,101)
leo_random_distance = random.randrange(1,101)
michelangelo.forward(mic_random_distance)
leonardo.forward(leo_random_distance)
time.sleep(3) #used this so we can see where they end before reseting
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
for i in range (0,10):
  mic_random_loop = random.randrange(0,11)
  leo_random_loop = random.randrange(0,11)
  michelangelo.forward(mic_random_loop)
  leonardo.forward(leo_random_loop)
time.sleep(3) # Also used so we can see where they end
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
print('Click turtle window to continue')
window.exitonclick()
# PART B - complete part B here

#imported pygame/math at top

pygame.init()
window = pygame.display.set_mode()

coords = []
num_sides = 4
side_length = 100
offset = 200
for i in range (1,5):
  theta = 2.0*math.pi * i /num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append((x,y))
pygame.draw.polygon(window, 'red', coords)
pygame.display.flip()
time.sleep(3)#pygame.wait wouldn't work for me so I used this instead
window.fill('black')
pygame.display.flip()
time.sleep(1)

coords = []
num_sides = (3, 4, 6, 9, 360)
side_length = 100
offset = 200
for sides in (num_sides):
  for i in range(sides):
    theta = 2.0*math.pi * i / sides
    x = side_length * math.cos(theta) + offset
    y = side_length * math.sin(theta) + offset
    coords.append((x,y))
  pygame.draw.polygon(window, "red", coords)
  pygame.display.flip()
  time.sleep(3)
  window.fill("black")
  pygame.display.flip()
  time.sleep(1)
  coords = []