# Monopoly Game Implementation

This is a simple implementation of the classic board game Monopoly using Python. The game logic is contained within two files: `monopoly_game.py` for the main game functionality and `bank.py` for managing game banking and property ownership.

## Features

- **Multiple Players**: Players can enter the number of participants at the beginning of the game, and the game supports up to 8 players.
- **Player Turns**: Players take turns rolling dice, moving their tokens on the board, and performing actions based on the space they land on.
- **Property Ownership**: Players can purchase properties when they land on them, and the game keeps track of which player owns which properties.
- **Community Chest and Chance**: Landing on specific board spaces triggers drawing Community Chest and Chance cards, which can result in various events such as gaining or losing money, moving to different board spaces, or getting out of jail.
- **Bankruptcy and Winning**: The game detects when a player goes bankrupt and declares a winner when only one player remains solvent.

## Installation

1. Clone or download the repository to your local machine.
2. Make sure you have Python 3.x installed.
3. Install the required dependencies using pip:
   ```bash
   pip install Pillow

## How to Play

1. Run the script `monopoly_game.py`.
2. Enter the number of players when prompted.
3. Follow the on-screen instructions to play the game.
4. Continue playing until a winner is declared or all players except one go bankrupt.

## File Structure

- `monopoly_game.py`: Main script for the Monopoly game, containing the game logic and user interface.
- `bank.py`: Module containing functions related to game banking and property management.
- `logo.png`: Image file used for the Monopoly logo.

## Dependencies

- **Python 3.x**


