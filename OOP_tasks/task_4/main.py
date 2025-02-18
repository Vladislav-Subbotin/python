import random
class warrior:
  def __init__(self):
    print('введите количество здоровия воина')
    self.health = int(input())
    print('введите количество брони воина')
    self.armor = int(input())
    print('введите количество выносливости воина')
    self.stamina = int(input())
  def hithit(self, enemy):
    #print('оба ударили')
    if self.stamina > 0:
      self.stamina-=10
      enemy.health-=random.randint(10, 30)
    else:
      enemy.health-=random.randint(0, 10)
    if enemy.stamina > 0:
      enemy.stamina-=10
      self.health-=random.randint(10, 30)
    else:
      self.health-=random.randint(0, 10)
  def hitdefense(self, enemy):
    #print('1 ударил другого')
    if self.stamina > 0:
      self.stamina-=10
      if enemy.armor > 0:
        enemy.health-=random.randint(0, 20)
        enemy.armor-=random.randint(0, 10)
      else:
        enemy.health-=random.randint(10, 30)
    else:
      enemy.health-=random.randint(0, 10)
unit1 = warrior()
unit2 = warrior()
while unit1.health > 10 and unit2.health > 10:
  #print(unit1.health,' - ',unit2.health)
  #print(unit1.armor,' - ',unit2.armor)
  #print(unit1.stamina,' - ',unit2.stamina)
  #print('\n')
  r1 = random.randint(1, 2)
  r2 = random.randint(1, 2)
  if r1 == 1 and r2 == 1:
    unit1.hithit(unit2)
  elif r1 == 1 and r2 == 2:
    unit1.hitdefense(unit2)
  elif r1 == 2 and r2 == 1:
    unit2.hitdefense(unit1)
else:
  if unit1.health <= 10:
    print('победил 2 воин')
  else:
    print('победил 1 воин')