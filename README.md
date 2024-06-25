# Nim Game and Subtract Square Game

Welcome to the repository for the Nim Game and Subtract Square Game. These are two fun and challenging games where players take turns to achieve victory.

## Nim Game

In the Nim Game, players take turns removing stones from a pile. The player who takes the last stone loses the game.

### How to Play

1. **Starting the Game:**
   - The game starts with a random number of stones (between 20 and 30).
   - Players choose between playing against another player or the computer.

2. **Taking Turns:**
   - Players can remove 1, 2, or 3 stones from the pile on their turn.
   - The game alternates turns between the two players (or player and computer).

3. **Winning the Game:**
   - The player who is forced to take the last stone loses the game.

### Example

```plaintext
Welcome in Nim Game, This is a game where players take turns taking stones from a pile of stones. The player who takes the last stone loses.
please enter your player1 name: Alice
please choose between 1 vs 1 or vs computer: 1 vs 1
please enter your player2 name: Bob
The current stone count is: 25

Alice, How many stones do you want to remove? 2
Alice removed 2 stones! The current stone count is: 23

Bob, How many stones do you want to remove? 3
Bob removed 3 stones! The current stone count is: 20

...

Alice took the last stone you lost. Bob won the game!
```

## Subtract Square Game

In the Subtract Square Game, players take turns removing a square number of coins. The player who takes the last coin wins the game.

### How to Play

1. **Starting the Game:**

  - The game starts with a random number of coins (between 30 and 200).
  - Players take turns in a sequence.

2. **Taking Turns:**

  - On their turn, each player must remove a number of coins that is a perfect square (e.g., 1, 4, 9, 16, etc.).
  - The game continues until all coins are taken.

3. **Winning the Game:**

  - The player who takes the last coin wins the game.

### Example
```plaintext
Subtract square game - Take a square number of coins 1, 4, 9, ... - Player who takes the last coin will win.
We have 50 coins.
Player 1 turn.
Take some coins: 9
We have 41 coins.
Player 2 turn.
Take some coins: 16
We have 25 coins.
Player 1 turn.

...

Player 2 wins.
```

## Repository Structure

- `nim_game.py`: Contains the implementation of the Nim Game.
- `subtract_square_game.py`: Contains the implementation of the Subtract Square Game.
- `README.md`: This file, providing an overview and instructions for the games.

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/nim-game.git
   ```

2. Navigate to the repository directory:
  ```bash
  cd nim-game
  ```

3. Run the desired game:
  ```bash
  python nim_game.py
  # or
  python subtract_square_game.py
  ```

## Acknowledgements

- Inspired by classic mathematical strategy games.
- Developed with Python for educational and entertainment purposes.
