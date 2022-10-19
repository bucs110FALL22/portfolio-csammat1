def main():
  print(multiplication(5))
  print(multiplication(3))
  print(exponentiate(2, 3))
  print(exponentiate(3, 2))
  print(square(2))
  print(square(5))
def multiplication(num):
  result = 0
  for i in range(num):
    result += num
  return result

def exponentiate(num, power):
  result = num
  for i in range(power-1):
    result = result*num
  return result
def square(num):
  return exponentiate(num, 2)
main()