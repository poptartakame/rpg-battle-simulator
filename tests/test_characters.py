import unittest

from characters.rogue import Rogue

# ARRANGE > ACT > ASSERT
# run test in root terminal :
# python3 -m unittest discover -s tests -v

class TestCharacters(unittest.TestCase):
    def test_take_damage(self):
        player = Rogue("Rogue")

        player.take_damage(20)

        self.assertEqual(player.health, 82)

    def test_minimum_damage(self):
        player = Rogue("Rogue")
        
        player.take_damage(1)
        
        self.assertEqual(player.health, 99)

    def test_overkill_damage(self):
        player = Rogue("Rogue")

        player.health = 10
        damage_dealt = player.take_damage(52)

        self.assertEqual(player.health, 0)
        self.assertEqual(damage_dealt, 10)