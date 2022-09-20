import random

random_number = random.randint(1,10)
guesses = 1
print('Guess the number between 1 and 10')
while guesses < 4:
  guess = int(input())
  if guess > random_number:
    print('The number is smaller')
    guesses += 1
  if guess < random_number:
    print('The number is larger')
    guesses += 1
  if guess == random_number:
    break
if guesses < 4:
  if guesses == 1:
    print("That's it, you got it in " + str(guesses) + " guess, lucky guess!")
  else:
    print("That's it, you got it in " + str(guesses) + " guesses")
if guesses == 4:
  print('The number was ' + str(random_number) + ' you suck...just kidding')