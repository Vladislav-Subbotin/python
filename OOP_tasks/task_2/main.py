import math
class Point:
  x = 0
  y = 0
  def add_to_x(self):
    print('координата x увеличена на')
    self.x += float(input())
  def add_to_y(self):
    print('координата y увеличена на')
    self.y += float(input())
  def set_coord(self): 
    print('введите координату x')
    self.x = float(input())
    print('введите координату y')
    self.y = float(input())
  def get_coord(self):
    print('(',self.x,',',self.y,')')
  def get_polar_coord(self):
    self.r = (self.x**2+self.y**2)**0.5
    self.phi = math.acos(self.x/self.r)/math.pi*180
    print('(',self.r,',',self.phi,')')
  def distance(self, point2):
    print(((self.x-point2.x)**2+(self.y-point2.y)**2)**0.5)
obj1 = Point()
obj2 = Point()
#obj1.add_to_x()
#obj1.add_to_y()
obj1.set_coord()
#obj2.set_coord()
#obj1.get_coord()
obj1.get_polar_coord()
#obj1.distance(obj2)