import random
import math
import matplotlib.pyplot as plt

def direct():
    while True:
        l = random.uniform(-1, 1)
        n = random.uniform(-1, 1)
        m = random.uniform(-1, 1)
        len = (l**2+n**2+m**2)**0.5
        if len < 1:
            break
        l = l / len
        n = n / len
        m = m / len
    return l,n,m

print('введите радиус сферы')
R = float(input())
N=1000
x0 = []
y0 = []
z0 = []
p = []
x = 0
y = 0
for i in range(100):
    z = i
    z0.append(i)
    count = 0
    for j in range(N):
        l,n,m = direct()
        a = l**2+n**2+m**2
        b = 2*(l*x+n*y+m*z)
        c = x**2+y**2+z**2-R**2
        d = b**2-4*a*c
        if d >= 0:
            t = (-b+d**2)/(2*a)
            if t > 0:
                count+=1
    p.append(count/N)
plt.plot(z0, p)
plt.show()