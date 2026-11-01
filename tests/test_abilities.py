import unittest

from characters.mage import Mage
from enemies.grunt import Grunt
from abilities import Fireball

# ARRANGE > ACT > ASSERT
# run test in root terminal :
# python3 -m unittest discover -s tests -v

class TestAbilities(unittest.TestCase):
    def test_fireball(self):
        mage = Mage("Mage")
        grunt = Grunt("Grunt")
        fireball = Fireball()

        fireball.use(mage, grunt)

        self.assertEqual(mage.mana, 130)
        self.assertEqual(grunt.health, 32)

    def test_fireball_insufficient_mana(self):
        mage = Mage("Mage")
        grunt = Grunt("Grunt")
        fireball = Fireball()

        mage.mana = 10
        result = fireball.use(mage, grunt)
        
        self.assertIsNone(result)
        self.assertEqual(grunt.health, 60)