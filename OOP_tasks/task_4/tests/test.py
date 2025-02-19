from pathlib import Path
import sys
import unittest
module_path = Path(__file__).parents[1]
sys.path.append(str(module_path))
from main import warrior

class TestWarrior(unittest.TestCase):
    def setUp(self):
        self.unit1 = warrior(200, 100, 200)
        self.unit2 = warrior(300, 0, 100)
    def test_hithit(self):
        initial_health_unit1 = self.unit1.health
        initial_health_unit2 = self.unit2.health
        initial_stamina_unit1 = self.unit1.stamina
        initial_stamina_unit2 = self.unit2.stamina
        self.unit1.hithit(self.unit2)
        self.assertLess(self.unit1.health, initial_health_unit1)
        self.assertLess(self.unit2.health, initial_health_unit2)
        self.assertLess(self.unit1.stamina, initial_stamina_unit1)
        self.assertLess(self.unit2.stamina, initial_stamina_unit2)
    def test_hitdefense(self):
        initial_health_unit2 = self.unit2.health
        initial_armor_unit2 = self.unit2.armor
        initial_stamina_unit1 = self.unit1.stamina
        self.unit1.hitdefense(self.unit2)
        self.assertLess(self.unit2.health, initial_health_unit2)
        if initial_armor_unit2 > 0:
            self.assertLess(self.unit2.armor, initial_armor_unit2)
        self.assertLess(self.unit1.stamina, initial_stamina_unit1)
unittest.main()