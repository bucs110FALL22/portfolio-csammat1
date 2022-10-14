import pygame
import time
pygame.init()

def function(start, upper_limit):
  max_so_far = 0
  scale = 30
  iters= {}
  for num in range (start,upper_limit+1):
    count = 0
    n = num
    while n != 1:
      count += 1
      if n % 2 == 0:
        n = n/2
      else:
        n = 3*n + 1
    iters[num*scale] = count*scale
    if count > max_so_far:
      max_so_far = num
  return_list = [iters, max_so_far]
  return return_list
return_value = function(2,20)

cord_dictionary = return_value[0]
max_value = return_value[1]
cord_list = [(key, value) for key, value in cord_dictionary.items()]

display = pygame.display.set_mode()

display.fill('white')

pygame.draw.lines(display, 'black', False, cord_list)

new_display = pygame.transform.flip(display, False, True)

display.blit( new_display , (0, 0))

font = pygame.font.Font(None, 12)
text = 'The max intergrations is @ ' + str(max_value)
msg = font.render(text, False, 'black')

display.blit(msg, (10,10))

pygame.display.flip()
time.sleep(10)