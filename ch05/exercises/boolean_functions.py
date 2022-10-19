
def percentage_to_letter(score=0):
  letter_grade = ''
  score = int(score)
  if score >= 90:
    letter_grade = 'A'
  elif score >= 80:
    letter_grade = 'B'
  elif score >= 70:
    letter_grade = 'C'
  elif score >= 60:
    letter_grade = 'D'
  else:
    letter_grade = 'F'
  return letter_grade
def is_passing(letter = ''):
  if letter == 'A' or letter == 'B' or letter == 'C':
    passing = True
  else:
    passing = False
  return passing
def input_data():
  print("Input your grade percentage:")
  percentage = input()
  letter_grade = percentage_to_letter(score=percentage)
  passing = is_passing(letter = letter_grade)
  if passing:
    print('You passed')
    print('You got the letter grade: ' + letter_grade)
  else:
    print('You failed')
    print('You got the letter grade: ' + letter_grade)
  input_data()
input_data()