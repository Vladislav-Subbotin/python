import matplotlib.pyplot as plt
import math

t2 = 5.2714


log = math.log(0.1, 2)
t = int(-log * t2)
time = list(range(1, t+1))
mass = list(range(1, t+1))
for i in range(0, t):
  mass[i] = (0.5)**(time[i]/t2)
plt.plot(time, mass, label='масса')
plt.xlabel('Время')
plt.ylabel('Масса')
plt.title('Зависимость массы Со-60 от времени')
plt.legend(fontsize=14)
plt.grid(which='major')
plt.semilogy()
plt.show()