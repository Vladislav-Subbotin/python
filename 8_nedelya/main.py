import matplotlib.pyplot as plt
import math

class Atom():
    mp = 938.272 #массы в Мэв
    mn = 939.565 #массы в Мэв
    me = 0.511 #массы в Мэв
    def atom_set(self, a, z):
        self.a = a
        self.z = z
        self.neutron = a - z
    def atom_bind_energy(self):
        self.be = 15.5 * self.a - 16.8 * (self.a ** (2/3)) - 0.72 * self.z * (self.z - 1) / (self.a ** (1/3)) - 23 * ((self.a - 2 * self.z) ** 2) / self.a
        if self.a % 2 == 0 and self.z % 2 == 0:
            self.be += 12 * (self.a ** (-1/2))
        elif self.a % 2 == 1 and self.z % 2 == 1:
            self.be -= 12 * (self.a ** (-1/2))
        self.epsilon = self.be / self.a
        #print('Удельная энергия связи = ', self.epsilon, 'Мэв')
        return self.epsilon
    def atom_mass(self):
        self.mass = self.z * self.mp + self.neutron * self.mn - self.be
        #print('масса ядра = ', self.mass, 'Мэв')
        return self.mass
    def atom_nuclear_radius(self):
        self.radius = 1.3e-5*(self.a**(1/3))
        #print('радиус ядра = ', self.radius, 'А')
        return self.radius
    def atom_beta_decay(self):
        self.z += 1
        self.neutron -= 1
        self.atom_bind_energy()
        self.atom_mass()
        self.mass_betam = self.mass
        self.z -= 2
        self.neutron += 2
        self.atom_bind_energy()
        self.atom_mass()
        self.mass_betap = self.mass
        self.z += 1
        self.neutron -= 1
        self.atom_bind_energy()
        self.atom_mass()
        if self.mass < self.mass_betam + self.me and self.mass < self.mass_betap - self.me:
            return 'Атом устойчив к бета распаду'
        else:
            return 'Атом неустойчив к бета распаду'
    def atom_nuclear_fission(self):
        if self.a % 4 != 0 or self.z % 4 !=0:
            return 'деление невозможно'
        else:
            self.neutron = self.neutron/2
            self.z = self.z/2
            self.a = self.a/2
            self.atom_bind_energy()
            self.atom_mass()
            self.mass_shard = self.mass
            self.neutron = self.neutron * 2
            self.z = self.z * 2
            self.a = self.a * 2
            self.atom_bind_energy()
            self.atom_mass()
            if self.mass < 2 * self.mass_shard:
                return 'деление невозможно'
            else:
                return 'деление возможно'
    def atom_be_plot(self):
        self.z0 = int(self.z)
        self.a0 = self.a
        self.q = list(range(1, self.z0))
        self.energy = list(range(1, self.z0))
        for self.z in range(1, self.z0):
            self.a = 2*self.z
            self.atom_bind_energy()
            self.energy[self.z-1] = self.atom_bind_energy()
        self.a = self.a0
        plt.plot(self.q, self.energy)
        plt.xlabel('количество нуклонов(А)')
        plt.ylabel('удельная энергия связи')
        plt.title('Значения удельных энергий связи для атомов главной диагонали')
        plt.legend(fontsize=14)
        plt.grid(which='major')
        plt.show()
    def atom_radius_plot(self):
        self.a0 = int(self.a)
        self.m = list(range(1, self.a0))
        self.r = list(range(1, self.a0))
        for self.a in range(1, self.a0):
            self.atom_nuclear_radius()
            self.r[self.a - 1] = self.atom_nuclear_radius()
        plt.plot(self.m, self.r)
        plt.xlabel('количество нуклонов(А)')
        plt.ylabel('радиус ядра')
        plt.title('зависимость радиуса ядра от числа нуклонов')
        plt.legend(fontsize=14)
        plt.grid(which='major')
        plt.show()
#u = Atom()
#u.atom_set(235, 92)
#print('Удельная энергия связи = ', u.atom_bind_energy(), 'Мэв')
#print('масса ядра = ', u.atom_mass(), 'Мэв')
#print('масса ядра = ', u.atom_mass()/931.494, 'а.е.м.')
#print('радиус ядра = ', u.atom_nuclear_radius(), 'А')
#print (u.atom_beta_decay())
#print(u.atom_nuclear_fission())
#u.atom_be_plot()
#u.atom_radius_plot()