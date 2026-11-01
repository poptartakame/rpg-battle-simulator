from characters.character import Character

class Enemy(Character):
    def __init__(self, name, level=1):
        super().__init__(name, level)

        self.max_health = 60
        self.health = 60
        self.max_mana = 20
        self.mana = 20
                
        self.strength = 7
        self.intelligence = 5
        self.defense = 3