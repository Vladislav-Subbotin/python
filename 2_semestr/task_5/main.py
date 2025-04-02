import random
import matplotlib.pyplot as plt

def energy(k, line):
    p = []
    E = []
    N = []
    p.append(random.randint(0, 10))
    E.append(random.uniform(0, 10))
    N.append(0)
    for i in range(1, line):
        p.append(random.randint(p[i-1], p[i-1]+10))
        E.append(random.uniform(E[i-1]+1, E[i-1]+10))
        N.append(0)
    for j in range(k):
        rand_numb = random.randint(0, p[line-1])
        i=0
        while(0==0):
            if rand_numb<=p[i]:
                N[i]+=1
                break
            else:
                i+=1
    plt.bar(E, N)
    plt.show()
energy(10000, 5)
energy(10000, 10)
energy(10000, 100)