x1 = (10 * 5)
print(x1)
x2 = (10 ** 2)
print(x2)
x3 = (15 / 10)
print(x3)
x4 = (15 // 10)
print(x4)
x5 = (-15 // 10)
print(x5)
x6 = (15 % 10) 
print(x6)
x7 = (10 % 15)
print(x7)
x8 = (10 % 10)
print(x8)
x9 = (0 % 10)
print(x9)
x10 = (10 / 15)
print(x10) #10/15 = 2/3 which is an infinite number. Python does not calculate it infinetly and does not round up. It stops once it reached 16 6s

while True:
  print('What is the current Euro to Dollar exchange rate [How many Euros = 1 US Dollar]')
  rate = float(input())
  int(rate)
  print('How much currency would you like to exchange? [Number of Euros]')
  amount = float(input())
  int(amount)
  total = amount/rate
  result = total - 3
  if result > 0:
    print('After the 3 dollar service fee your total returned it ' + str(result) + ' thank you for using our service.')
    break
  if result < 0:
    print('We charge a 3 dollar service fee, unable to exchange this amount. Please try again.')