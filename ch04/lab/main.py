import random
import pygame
import time
import math

def clean_dart_screen():
  window.fill('aquamarine')
  window.fill('aquamarine')
  pygame.draw.circle(window, 'yellow', (circle_width, circle_height), (circle_radius))
  
  pygame.draw.line(window, 'black', (width/2-circle_radius, height/2), (width-80, height/2))
  
  pygame.draw.line(window, 'black', (width/2,0), (width/2, height))
  
  pygame.display.flip()
  time.sleep(5)
pygame.init()
window = pygame.display.set_mode((640, 480))

width = pygame.display.get_window_size()[0]
height = pygame.display.get_window_size()[1]

circle_width=width/2
circle_height= height/2
circle_radius=height/2
clean_dart_screen()
for i in range(0,10):
  x_dart = random.randrange(0,width)
  y_dart = random.randrange(0,height)
  r_dart=3
  distance_from_center = math.hypot(x_dart-circle_width, y_dart-circle_height)
  
  if distance_from_center <= circle_radius:
    dart_color="black"
  else:
    dart_color='red'
  pygame.draw.circle(window, dart_color, (x_dart, y_dart), (r_dart))
  pygame.display.flip()
time.sleep(10)
clean_dart_screen()
red_button = pygame.Rect(0,0, width/2, height)
blue_button = pygame.Rect(width/2, 0, width/2, height)
pygame.draw.rect(window, 'red', red_button)
pygame.draw.rect(window, 'blue', blue_button)
pygame.display.flip()
print('Pick your Team')
team = ''
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      mouse_click_pos = event.pos
      if red_button.collidepoint(mouse_click_pos):
        team = 'red'
      if blue_button.collidepoint(mouse_click_pos):
        team = 'blue'
  if team == 'red':
    break
  if team == 'blue':
    break          
clean_dart_screen()
red_score=0
blue_score=0
r_dart=3
for i in range(0,10):
  red_x_dart = random.randrange(0,width)
  red_y_dart = random.randrange(0,height)
  blue_x_dart = random.randrange(0,width)
  blue_y_dart = random.randrange(0,height)
  
  distance_from_center_red = math.hypot(red_x_dart-circle_width, red_y_dart-circle_height)
  if distance_from_center_red <= circle_radius:
    red_score += 1
    red_dart_color = 'red'
  else:
    red_dart_color = 'darkred'
  pygame.draw.circle(window, red_dart_color, (red_x_dart, red_y_dart), (r_dart))
  pygame.display.flip()
  time.sleep(1)
  
  distance_from_center_blue = math.hypot(blue_x_dart-circle_width, blue_y_dart-circle_height)
  if distance_from_center_blue <= circle_radius:
    blue_score += 1
    blue_dart_color = 'blue'
  else:
    blue_dart_color = 'darkblue'
  pygame.draw.circle(window, blue_dart_color, (blue_x_dart, blue_y_dart), (r_dart))
  pygame.display.flip()
  print('Red Score = ' + str(red_score))
  print('Blue Score = ' + str(blue_score))
  time.sleep(2)
if team == 'red':
  if red_score > blue_score:
    print('You Win!')
  elif red_score == blue_score:
    print('You Tied :|')
  else:
    print('You Lose :(')
if team == 'blue':
  if blue_score > red_score:
    print('You Win!')
  elif blue_score == red_score:
    print('You Tied :|')
  else:
    print('You Lose :(')
time.sleep(10)