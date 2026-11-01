import unittest

from characters.rogue import Rogue
from items import HealthPotion

# ARRANGE > ACT > ASSERT
# run test in root terminal :
# python3 -m unittest discover -s tests -v

class TestItems(unittest.TestCase):
    def test_health_potion(self):
        player = Rogue("Rogue")
        potion = HealthPotion()

        player.health = 50

        potion.use(player)

        self.assertEqual(player.health, 80)

    def test_health_potion_max_health(self):
        player = Rogue("Rogue")
        potion = HealthPotion()

        player.health = 90

        potion.use(player)

        self.assertEqual(player.health, 100)

    def test_health_potion_full_health(self):
        player = Rogue("Rogue")
        potion = HealthPotion()
        
        player.health = player.max_health
        
        potion.use(player)
        
        self.assertFalse(potion.use(player))

    def test_health_potion_inventory(self):
        player = Rogue("Rogue")
        potion = HealthPotion()

        player.add_item(potion)
        player.add_item(potion)
        player.health = 50
                
        player.use_item(potion, player)

        self.assertEqual(player.health, 80)       
        self.assertEqual(player.inventory["Health Potion"], 1)

    def test_health_potion_inventory_failure(self):
        player = Rogue("Rogue")
        potion = HealthPotion()

        player.add_item(potion)
        player.add_item(potion)
        player.health = player.max_health

        player.use_item(potion, player)

        self.assertEqual(player.health, 100)
        self.assertEqual(player.inventory["Health Potion"], 2)
        self.assertFalse(player.use_item(potion, player))