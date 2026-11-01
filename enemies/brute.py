from enemies.enemy import Enemy

class Brute(Enemy):
    def __init__(self, name, level=1):
        super().__init__(name, level)

        self.max_health = 120
        self.health = 120
        self.max_mana = 10
        self.mana = 10
                
        self.strength = 11
        self.intelligence = 3
        self.defense = 6