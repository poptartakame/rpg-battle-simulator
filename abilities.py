from status_effects import DefenseBoost

class Ability:
    def __init__(self, name, mana_cost, description):
        self.name = name
        self.mana_cost = mana_cost
        self.description = description

    def use(self, user, target):
        if user.mana < self.mana_cost:
            print(f"\nNot enough mana!")
            return None

        user.mana -= self.mana_cost
        
        damage = self.calculate_damage(user)
        damage_dealt = target.take_damage(damage)

        self.special_effect(user)

        return damage_dealt

    def special_effect(self, user):
        return None

class DefensiveStrike(Ability):
    def __init__(self):
        super().__init__(
            
            name = "Defensive Strike",
            mana_cost = 5,
            description = "A weaker attack that temporarily raises defense until attacked."
        )

    def calculate_damage(self, user):
        return user.strength * 0.5

    def special_effect(self, user):
        boost = DefenseBoost("Defense Boost", 4)
        user.add_status_effect(boost)

class Fireball(Ability):
    def __init__(self):
        super().__init__(

            name = "Fireball",
            mana_cost = 20,
            description = "Launches a powerful fireball at an enemy."
        )

    def calculate_damage(self, user):
        return user.intelligence * 1.5

class PrecisionStrike(Ability):
    def __init__(self):
        super().__init__(

            name = "Precision Strike",
            mana_cost = 15,
            description = "A precise attack that combines strength and agility to deal increased damage."
        )

    def calculate_damage(self, user):
        return user.strength * 0.5 + user.agility * 0.7