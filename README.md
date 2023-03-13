# Connect-4 Game in Python

## Introduction

Connect 4 is a board game for multiple players and can be played here to get intuition about it:
https://www.cbc.ca/kids/games/play/connect-4

It is typically a game for two players played on a two-dimensional board. In the link to game mentioned above, the board size is 6x7 which means that the board has 6 rows and 7 columns. Each player take turn by dropping a checker into a column of the board. The checkers fall straight down, occupying the lowest available space in the column. Any player who gets 4 checkers in a row which could be either horizontally, vertically or diagonally in first place will win the game.

## Project Goal

The goal of this project is to implement the Connect 4 game in Python3. In our project, the python topics like `lists`, `decision structures`, `loops`, `user-defined functions`, `variable scopes` and `other programming concepts` in Python are covered.
Additionally, it is a good exercise in decomposing larger problems into smaller and manageable parts.

## How Game Works

At the beginning of the game, a two-dimensional board is created with number of rows and columns specified as global constants, it can be any size up to a maximum of 26 columns (to work as intended). The board indexes are initialized with whitespaces (" "). The game can be played between 2 to 5 players, and each player will be assigned with the available checker: "#", "O", "X", "Q", and "*". The goal of the game is to place 4 checkers in a row horizontally, vertically, or diagonally.

Before the game starts, a random player is chosen, and the board is printed to show the user what it looks like. The columns of the board are labeled with letters, starting with A.

During each turn, the player must place their checker in a column of their choice by entering a letter. Valid input will be checked. If the column is already completely filled with checkers, the player loses the turn because the checker cannot be placed in that column.

After every turn, the game is checked for a possible win. If the board fills up before either player achieves 4 checkers in a row, the game is a draw.

## How Game Ends

The game ends if either any player wins or a game is draw.

