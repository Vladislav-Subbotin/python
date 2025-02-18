date = input('Введите дату в формате дд.мм.гггг:')
leap = False

date = date.split('.')
date[2] = int(date[2])
date[1] = int(date[1])
date[0] = int(date[0])

if (date[2] % 4 == 0 and date[2] % 100 != 0) or date[2] % 400 == 0:
    leap = True

if date[1] < 1 or date[1] > 12:
  print("Даты не существует")
elif date[0] < 1 or (date[1] == 2 and (date[0] > 28 and leap == False) or (date[0] > 29 and leap == True)) or (date[0] > 30 and (date[1] == 4 or date[1] == 6 or date[1] == 9 or date[1] == 11)) or date[0]>31:
  print("Даты не существует")
else: 
  print("Дата существует")