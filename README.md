# RPG Battle Simulator

## Overview

RPG Battle Simulator is a terminal-based, turn-based combat game developed in Python. It features multiple character classes, enemy types, unique abilities, an inventory system, and status effects.

This is my first independent Python project, developed as a proof of concept to demonstrate the knowledge and skills I've gained through my Python coursework. The goal was to put these concepts into practice by designing and building a functional program, with an emphasis on object-oriented programming, modular code organization, problem-solving, and automated testing.

## Features

- **Turn-Based Combat:** Battle enemies using basic attacks, special abilities, and consumable items.
- **Character Classes:** Three playable classes (Warrior, Mage, and Rogue), each with unique stats and abilities.
- **Enemy Types:** Three enemy classes (Grunt, Brute, and Acolyte) with different attributes.
- **Abilities and Status Effects:** Class-specific abilities with mana costs, damage calculations, and temporary effects.
- **Inventory System:** Collect and use Health Potions and Mana Potions during combat.
- **Character Progression:** Leveling system with stat increases and a maximum level of 20.
- **Automated Testing:** Unit tests covering character damage, abilities, and item functionality.

## Installation and Usage

### Requirements

- Python 3

### Getting Started

1. Download the repository as a ZIP file from GitHub and extract it, or clone the repository using Git.
2. Open a terminal and navigate to the project's root directory.
3. Run the following command:

   ```bash
   python3 main.py
   ```

**Note:** Depending on your Python installation, Windows users may need to use `python main.py` or `py main.py` instead.

### Gameplay

The game starts with a Warrior facing a Grunt. The Warrior is equipped with Defensive Strike, two Health Potions, and one Mana Potion.

During combat, players can perform basic attacks, use abilities, consume items, view character stats, or retreat from battle.

Other character classes, enemies, and abilities can be explored by modifying the starting configuration in `main.py`.

## Automated Testing

The project includes 10 automated unit tests using Python's built-in `unittest` framework.

These tests cover:

- Character damage calculations, including minimum damage and overkill damage.
- Health Potion functionality, healing limits, and inventory management.
- Ability damage calculations and insufficient mana handling.

To run all tests, navigate to the project's root directory and execute:

```bash
python3 -m unittest discover -s tests -v
```

## Project Structure

```text
rpg-battle-simulator/
├── .gitignore
├── README.md
├── main.py
├── combat.py
├── display.py
├── abilities.py
├── status_effects.py
├── items.py
├── characters/
│   ├── __init__.py
│   ├── character.py
│   ├── warrior.py
│   ├── mage.py
│   └── rogue.py
├── enemies/
│   ├── __init__.py
│   ├── enemy.py
│   ├── grunt.py
│   ├── brute.py
│   └── acolyte.py
└── tests/
    ├── test_characters.py
    ├── test_abilities.py
    └── test_items.py
```

The project uses a modular structure to separate combat logic, character and enemy classes, abilities, status effects, and inventory management. Automated tests are organized separately in the `tests/` directory.