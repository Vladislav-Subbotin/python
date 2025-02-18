koef = [float(input()), float(input()), float(input()), float(input()), float(input())]
dy = [koef[0]*4, koef[1]*3, koef[2]*2, koef[3]]
p = (3*dy[0]*dy[2]-dy[1]**2)/(3*(dy[0]**2))
q = 2*(dy[1]**3)-9*dy[0]*dy[1]*dy[2]+27*(dy[0]**2)*dy[3]
koeft = [1, 0, p, q]
dis = (p/3)**3+(q/2)**2
alpha = (-q/2+(dis)**0.5)**(1/3)
beta = (-q/2-(dis)**0.5)**(1/3)
if dis > 0:
    x1 = alpha+beta-b/a/3

elif dis == 0:
    x1 = alpha+beta-b/a/3
    x2 = -alpha-b/a/3

else:
    x1 =