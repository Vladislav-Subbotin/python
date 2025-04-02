import random
import math
import matplotlib.pyplot as plt

def direct():
    phi = math.pi*random.uniform(-1, 1)
    teta = math.pi*random.uniform(0, 1)
    return phi,teta
x = []
y = []
z = []
for i in range(5000):
    phi, teta = direct()
    x.append(math.sin(teta)*math.cos(phi))
    y.append(math.sin(teta)*math.sin(phi))
    z.append(math.cos(teta))
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.scatter(x, y, z, s=1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()