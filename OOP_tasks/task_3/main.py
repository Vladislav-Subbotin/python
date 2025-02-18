import random
class warrior:
  def __init__(self):
    self.health = 100
  def hit(self, enemy):
    for i in range(0, 9):
      r = random.randint(1, 2)
      if r == 1 and enemy.health > 0:
        enemy.health=enemy.health-20
        if enemy.health == 0:
          print('победил 1 воин')
          break
        print('юнит 1 атоковал, здоровье юнита 2 ', enemy.health)
      elif self.health > 0:
        self.health=self.health-20
        if self.health == 0:
          print('победил 2 воин')
          break
        print('юнит 2 атоковал, здоровье юнита 1 ', self.health)
unit1 = warrior()
unit2 = warrior()
unit1.hit(unit2)