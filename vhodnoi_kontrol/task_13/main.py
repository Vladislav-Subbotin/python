import matplotlib.pyplot as plt
import math

x = list(range(-5, 6))
y = list(range(-5, 6))
for i in range(0, len(x)):
  y[i] = math.cos(x[i]**2)+math.cos(x[i]+(2*math.pi)/3)+math.cos(x[i]+(4*math.pi)/3)
plt.plot(x, y, label='y=y(x)')
plt.xlabel('Ось - x')
plt.ylabel('Ось - y')
plt.title('График')
plt.legend(fontsize=14)
plt.grid(which='major')
plt.show()