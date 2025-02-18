from pathlib import Path
import sys
import unittest

module_path = Path(__file__).parents[1]
sys.path.append(str(module_path))
from main import Atom
class TestAtom(unittest.TestCase):
    def setUp(self):
        self.atom = Atom()
        self.atom.atom_set(235, 92)
    def test_atom_set(self):
        self.assertEqual(self.atom.a, 235)
        self.assertEqual(self.atom.z, 92)
        self.assertEqual(self.atom.neutron, 143)
    def test_atom_bind_energy(self):
        epsilon = self.atom.atom_bind_energy()
        self.assertAlmostEqual(epsilon, 7.590, places=0)
    def test_atom_mass(self):
        self.atom.atom_bind_energy()
        mass = self.atom.atom_mass()/931.494
        self.assertAlmostEqual(mass, 235.044, places=1)
    def test_atom_nuclear_radius(self):
        radius = self.atom.atom_nuclear_radius()
        self.assertAlmostEqual(radius, 7.4e-5, places=2)
    def test_atom_beta_decay(self):
        decay = self.atom.atom_beta_decay()
        self.assertEqual(decay, 'Атом устойчив к бета распаду')
    def test_atom_nuclear_fission(self):
        fission = self.atom.atom_nuclear_fission()
        self.assertEqual(fission, 'деление невозможно')