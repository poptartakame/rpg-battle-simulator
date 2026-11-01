from characters.character import Character

class Mage(Character):
    def __init__(self, name, level=1):
        super().__init__(name, level)

        self.max_health = 80
        self.health = 80
        self.max_mana = 150
        self.mana = 150
        
        self.strength = 5
        self.intelligence = 20
        self.defense = 3

        self.mana_regen = 5

    def level_up(self):
        previous_level = self.level

        super().level_up()

        if self.level > previous_level:
            self.max_mana += 15
            self.mana += 15

            self.intelligence += 2

            self.mana_regen += 2

    def calculate_damage(self):
        return self.intelligence * 0.4

    def attack(self, target):
        damage_dealt = super().attack(target)
        if damage_dealt > 0:
            self.restore_mana(self.mana_regen)
        return damage_dealt