from combat import Combat
from abilities import DefensiveStrike
from items import HealthPotion, ManaPotion

from characters.warrior import Warrior
from enemies.grunt import Grunt

def main():
    warrior = Warrior("Warrior")
    grunt = Grunt("Grunt")

    defensive_strike = DefensiveStrike()
    health_potion = HealthPotion()
    mana_potion = ManaPotion()

    warrior.learn_ability(defensive_strike)

    warrior.add_item(health_potion)
    warrior.add_item(health_potion)
    warrior.add_item(mana_potion)

    battle = Combat(warrior, grunt)
    print(battle.battle_start())

if __name__ == "__main__":
    main()

    # python3 main.py