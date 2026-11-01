from characters.character import Character

class Rogue(Character):
    def __init__(self, name, level=1):
        super().__init__(name, level)

        self.max_health = 100
        self.health = 100
        self.max_mana = 60
        self.mana = 60
        
        self.strength = 12
        self.intelligence = 8
        self.defense = 4

        self.agility = 18

    def level_up(self):
        previous_level = self.level

        super().level_up()

        if self.level > previous_level:
            self.agility += 2

    def calculate_damage(self):
        return self.strength * 0.5 + self.agility * 0.7