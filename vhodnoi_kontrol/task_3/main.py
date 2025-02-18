number = int(input())
prime = True

for i in range(2, int(number ** 0.5) + 1):
  if number % i == 0:
    prime = False
    break

if prime:
  print(number, "является простым числом.")
else:
  print(number, "не является простым числом.")