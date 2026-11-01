class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def use(self, user):
        restored = self.restore(user)
        effect_applied = self.special_effect(user)

        return restored > 0 or effect_applied

    def restore(self, user):
        return 0

    def special_effect(self, user):
        return False

    def can_use(self, user):
        return True

    def failure_message(self):
        return "This item cannot be used right now."

class HealthPotion(Item):
    def __init__(self):
        super().__init__(

            name = "Health Potion",
            description = "Restores 30 HP."
            )
        
    def restore(self, user):
        return user.restore_health(30)

    def can_use(self, user):
        return user.health < user.max_health

    def failure_message(self):
        return "Health is already full!"

class ManaPotion(Item):
    def __init__(self):
        super().__init__(
                
            name = "Mana Potion",
            description = "Restores 30 MP."
            )
            
    def restore(self, user):
        return user.restore_mana(30)

    def can_use(self, user):
        return user.mana < user.max_mana

    def failure_message(self):
        return "Mana is already full!"

ITEM_REGISTRY = {
    "Health Potion": HealthPotion,
    "Mana Potion": ManaPotion
}