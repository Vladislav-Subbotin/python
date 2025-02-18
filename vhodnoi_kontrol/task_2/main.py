month = int(input())

if month > 12 or month < 1:
  print("Неверный номер месяца")
elif month > 2 and month < 6:
    print("Весна")
elif month > 5 and month < 9:
    print("Лето")
elif month > 8 and month < 12:
    print("Осень")
else:
  print("Зима")