class Character:
    def __init__(self, name, level=1):
        self.name = name
        self.level = level

        self.max_health = 100
        self.health = 100
        self.health_regen = 2
        self.max_mana = 50
        self.mana = 50
        self.mana_regen = 2

        self.strength = 10
        self.intelligence = 10
        self.agility = 0
        self.defense = 5

        self.abilities = []
        self.status_effects = []

        self.inventory = {}

    def get_stats(self):
        ability_names = [ability.name for ability in self.abilities]
        formatted_abilities = ", ".join(ability_names) if ability_names else "None"

        item_list = [f"{item}: {quantity}" for item, quantity in self.inventory.items()]
        formatted_items = ", ".join(item_list) if item_list else "None"

        stats = (
            f"==============================\n"
            f"\nPlayer Stats:\n"

            f"\nName: {self.name}\n"
            f"Level: {self.level}\n"

            f"\nMax Health: {self.max_health}\n"
            f"Current Health: {self.health}\n"
            f"Health Regen: {self.health_regen}\n"
            f"Max Mana: {self.max_mana}\n"
            f"Current Mana: {self.mana}\n"
            f"Mana Regen: {self.mana_regen}\n"

            f"\nStrength: {self.strength}\n"
            f"Intelligence: {self.intelligence}\n"
            f"Agility: {self.agility}\n"
            f"Defense: {self.defense}\n"

            f"\nAbility List: {formatted_abilities}\n"
            f"\nInventory: {formatted_items}\n"
            
        )

        return stats

    def level_up(self):
        if self.level >= 20:
            print(f"{self.name} is already max level.")
        else:
            self.level += 1

            self.max_health += 10
            self.health += 10
            self.max_mana += 5
            self.mana += 5

            self.strength += 2
            self.intelligence += 2
            self.defense += 1

            print(f"{self.name} has leveled up to level: {self.level}!")

    def has_health(self):
        if self.health <= 0:
            return False
        return True

    def has_mana(self):
        if self.mana <= 0:
            return False
        return True

    def take_damage(self, amount):
        if amount <= 0:
            effective_damage = 0
        else:
            effective_damage = max(1, round(amount - self.defense * 0.5))

        damage_taken = min(self.health, effective_damage)
        self.health -= damage_taken

        for effect in self.status_effects[:]:
            effect.on_damage_taken(self)

        return damage_taken

    def restore_health(self, amount):
        missing_health = self.max_health - self.health

        if amount <= 0:
            effective_restoration = 0
        else:
            effective_restoration = max(1, round(amount))

        health_restored = min(missing_health, effective_restoration)
        self.health += health_restored

        if health_restored > 0:
            print(f"{self.name} restored {health_restored} HP!")

        return health_restored

    def restore_mana(self, amount):
        missing_mana = self.max_mana - self.mana
    
        if amount <= 0:
            effective_restoration = 0
        else:
            effective_restoration = max(1, round(amount))
    
        mana_restored = min(missing_mana, effective_restoration)
        self.mana += mana_restored

        if mana_restored > 0:
            print(f"{self.name} restored {mana_restored} MP!")
        return mana_restored

    def calculate_damage(self):
        return self.strength * 1.0

    def attack(self, target):
        if target.has_health():
            damage = self.calculate_damage()
            
            damage_dealt = target.take_damage(damage)

        else:
            damage_dealt = 0
            print(f"{target.name} health is already 0.")

        return damage_dealt

    def learn_ability(self, ability):
        if ability in self.abilities:
            print(f"{ability.name} already learned.")
        else:
            self.abilities.append(ability)
            print(f"{ability.name} learned.")

    def use_ability(self, ability, target):
        if ability in self.abilities:
            return ability.use(self, target)
        else:
            print(f"{ability.name} not learned.")
            return None

    def add_status_effect(self, effect):
        for active_effect in self.status_effects[:]:
            if type(active_effect) == type(effect):
                self.remove_status_effect(active_effect)

        self.status_effects.append(effect)
        effect.apply(self)

    def remove_status_effect(self, effect):
        if effect in self.status_effects:
            self.status_effects.remove(effect)
            effect.remove(self)

    def add_item(self, item):
        self.inventory[item.name] = self.inventory.get(item.name, 0) + 1
        print(f"x1 {item.name} added to inventory.")

    def use_item(self, item, user):
        if item.name in self.inventory:
            success = item.use(user)

            if not success:
                return False

            self.inventory[item.name] -= 1

            if self.inventory[item.name] <= 0:
                del self.inventory[item.name]

            return True

        else:
            return False