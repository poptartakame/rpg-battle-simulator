from characters.character import Character

class Warrior(Character):
    def __init__(self, name, level=1):
        super().__init__(name, level)

        self.max_health = 150
        self.health = 150
        self.max_mana = 30
        self.mana = 30
        
        self.strength = 15
        self.intelligence = 5
        self.defense = 8

    def level_up(self):
        previous_level = self.level

        super().level_up()

        if self.level > previous_level:
            self.max_health += 10
            self.health += 10

            self.strength += 2

    def calculate_damage(self):
        return self.strength * 1.2