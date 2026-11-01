class StatusEffect:
    def __init__(self, name):
        self.name = name

    def apply(self, character):
        pass

    def remove(self, character):
        pass

    def on_damage_taken(self, character):
        pass

class DefenseBoost(StatusEffect):
    def __init__(self, name, amount):
        super().__init__(name)
        self.amount = amount

    def apply(self, character):
        character.defense += self.amount

    def remove(self, character):
        character.defense -= self.amount

    def on_damage_taken(self, character):
        character.remove_status_effect(self)