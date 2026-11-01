from enemies.enemy import Enemy

class Acolyte(Enemy):
    def __init__(self, name, level=1):
        super().__init__(name, level)

        self.max_health = 45
        self.health = 45
        self.max_mana = 60
        self.mana = 60
                
        self.strength = 4
        self.intelligence = 14
        self.defense = 2

    def calculate_damage(self):
        return self.intelligence * 0.5