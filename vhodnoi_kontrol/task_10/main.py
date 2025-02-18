a = int(input())
b = int(input())
c = int(input())

d = b ** 2 - 4 * a * c
if d < 0:
  print("Уравнение не имеет действительных корней")
else:
  print('x1=',(-b+(d**0.5))/(2*a))
  print('x1=',(-b-(d**0.5))/(2*a))
