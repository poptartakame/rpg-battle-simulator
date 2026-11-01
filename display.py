def create_bar(current, max, width=20):

    filled = round((current / max) * width)
    bar = "█" * filled + "░" * (width - filled)

    return bar

def display_status(player, enemy):

    return (
        f"{player_display_status(player)}\n"
        f"{enemy_display_status(enemy)}\n"
    )

def player_display_status(player):

    player_hp_bar = create_bar(player.health, player.max_health)
    player_mp_bar = create_bar(player.mana, player.max_mana)

    return (
        f"{player.name} (Level {player.level})\n"
        f"HP: {player_hp_bar} {player.health}/{player.max_health}\n"
        f"MP: {player_mp_bar} {player.mana}/{player.max_mana}\n"
    )

def enemy_display_status(enemy):

    enemy_hp_bar = create_bar(enemy.health, enemy.max_health)

    return (
        f"{enemy.name} (Level {enemy.level})\n"
        f"HP: {enemy_hp_bar} {enemy.health}/{enemy.max_health}"
    )