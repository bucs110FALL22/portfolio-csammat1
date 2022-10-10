def star_pyramid():
  print('How many rows of stars would you like?')
  num_of_rows = int(input())
  stars = '*'
  for i in range(0,num_of_rows):
    print(stars)
    stars = stars + '*'
def rstar_pyramid():
  print('How many rows of stars would you like?')
  num_of_rows = int(input())
  stars = '*'*num_of_rows
  for i in range(0, num_of_rows):
    print(stars)
    stars_minus = stars[:-1]
    stars = stars_minus

star_pyramid()
rstar_pyramid()