import display
from items import ITEM_REGISTRY

class Combat:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

        self.turn_counter = 0
        self.round_counter = 0

    def turn_count(self):
        self.turn_counter += 1
        return self.turn_counter

    def round_count(self):
        self.round_counter += 1
        return self.round_counter

    def battle_start(self):
        choice = None

        while self.player.has_health() and self.enemy.has_health():

            choice = self.player_menu()

            if choice == "attack":
                self.turn_count()
                damage_dealt = self.player.attack(self.enemy)
                print(f"\n{self.player.name} attacks {self.enemy.name} for {damage_dealt} damage.")

            elif choice == "abilities":
                selected_ability = self.ability_menu()

                if selected_ability is None:
                    continue

                damage_dealt = self.player.use_ability(
                    selected_ability,
                    self.enemy
                )

                if damage_dealt is None:
                    continue

                self.turn_count()

                print(
                    f"\n{self.player.name} uses {selected_ability.name} "
                    f"on {self.enemy.name} for {damage_dealt} damage."
                )
            
            elif choice == "use item":
                selected_item = self.item_menu()

                if selected_item is None:
                    continue

                if selected_item.name not in self.player.inventory:
                    print(f"{selected_item.name} does not exist in inventory!")
                    continue

                if not selected_item.can_use(self.player):
                    print(f"\n{selected_item.failure_message()}")
                    continue

                print(f"\n{self.player.name} used {selected_item.name}!")

                success = self.player.use_item(
                    selected_item, 
                    self.player
                )

                if not success:
                    continue

                self.turn_count()

            elif choice == "view stats":
                print(f"\n{self.player.get_stats()}")
                continue

            elif choice == "retreat":
                self.turn_count()
                break

            if not self.enemy.has_health():
                break


            self.turn_count()
            print(f"\n==============================\n")
            print(f"ROUND {self.round_counter + 1}")
            print(f"TURN {self.turn_counter} — ENEMY")
            print(f"\n------------------------------\n")

            damage_dealt = self.enemy.attack(self.player)
            print(f"{self.enemy.name} attacks {self.player.name} for {damage_dealt} damage.")
            self.round_count()


        if choice == "retreat":
            print(f"\n==============================\n")
            print(f"{self.player.name} has retreated from battle.")
            print(f"\n==============================\n")

        elif not self.player.has_health():
            print(f"\n==============================\n")
            print(f"{self.player.name} has been defeated.")
            print(f"\n==============================\n")

        else:
            print(f"\n==============================\n")
            print(f"{self.enemy.name} has been defeated.")
            print(f"\n==============================\n")

        return (
            f"Battle Summary:\n"
            f"\nTOTAL ROUNDS: {self.round_counter}\n"
            f"TOTAL TURNS: {self.turn_counter}\n"
            f"\n==============================\n"
            )

    def player_menu(self):
        while True:

            print(f"\n==============================\n")
            print(f"ROUND {self.round_counter + 1}")
            print(f"TURN {self.turn_counter + 1} — PLAYER")
            print(f"\n==============================\n")

            print(display.display_status(self.player, self.enemy))

            print(f"\n==============================\n")
            print(f"Player Menu:")
            print(f"\n==============================\n")

            print(f"1. Attack")
            print(f"2. Abilities")
            print(f"3. Use Item")
            print(f"4. View Stats")
            print(f"5. Retreat")

            print(f"\n==============================\n")

            num = input("Select Option: ")

            if num == "1":
                return "attack"

            elif num == "2":
                return "abilities"
            
            elif num == "3":
                return "use item"
            
            elif num == "4":
                return "view stats"
            
            elif num == "5":
                return "retreat"
            
            else:
                print(f"\nInvalid choice. Please try again.")

    def ability_menu(self):
        while True:
            print(f"\n==============================\n")
            print(f"Abilities:\n")

            for index, ability in enumerate(self.player.abilities, start=1):
                print(f"{index}. {ability.name} - {ability.mana_cost} MP")

            print(f"{len(self.player.abilities) + 1}. Back")
            print(f"\n==============================\n")

            num = input("Select Option: ")
            back_option = str(len(self.player.abilities) + 1)

            if num == back_option:
                return None
            
            elif num.isdigit() and 1 <= int(num) <= len(self.player.abilities):
                selected_ability = self.player.abilities[int(num) - 1]

                while True:
                    print(f"\n==============================\n")
                    print(f"Ability Options: {selected_ability.name}\n")

                    print(f"1. Use Ability")
                    print(f"2. View Description")
                    print(f"3. Back")

                    print(f"\n==============================\n")
                    num = input("Select Option: ")

                    if num == "1":
                        return selected_ability
                    elif num == "2":
                        print(f"\n==============================\n")
                        print(f"{selected_ability.name} Description:\n")
                        print(selected_ability.description)
                    elif num == "3":
                        break
                    else:
                        print(f"\nInvalid choice. Please try again.")
            
            else:
                print(f"\nInvalid choice. Please try again.")

    def item_menu(self):
        while True:
            print(f"\n==============================\n")
            print(f"Items:\n")
    
            for index, (item, quantity) in enumerate(self.player.inventory.items(), start=1):
                print(f"{index}. {item}: {quantity}")
    
            print(f"{len(self.player.inventory) + 1}. Back")
            print(f"\n==============================\n")
    
            num = input("Select Option: ")
            back_option = str(len(self.player.inventory) + 1)
    
            if num == back_option:
                return None
                
            elif num.isdigit() and 1 <= int(num) <= len(self.player.inventory):
                item_names = list(self.player.inventory.keys())
                selected_item_name = item_names[int(num) - 1]
                selected_item = ITEM_REGISTRY[selected_item_name]()
    
                while True:
                    print(f"\n==============================\n")
                    print(f"Item Options: {selected_item.name}\n")
    
                    print(f"1. Use Item")
                    print(f"2. View Description")
                    print(f"3. Back")
    
                    print(f"\n==============================\n")
                    num = input("Select Option: ")

                    if num == "1":
                        return selected_item
                    elif num == "2":
                        print(f"\n==============================\n")
                        print(f"{selected_item.name} Description:\n")
                        print(selected_item.description)
                    elif num == "3":
                        break
                    else:
                        print(f"\nInvalid choice. Please try again.")
                
            else:
                print(f"\nInvalid choice. Please try again.")