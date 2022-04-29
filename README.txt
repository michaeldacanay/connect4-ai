# connect4-ai
Connect 4 is a two-player game in which players alternately place pieces on a vertical board. The player that first connects four pieces in a row wins. The board has 6 rows and 7 columns.

format: ```python3 connect4.py <ALG1> <D1> <EVAL1> <ALG2> <D2> <EVAL2>```
ex. python3 connect4.py MM 5 wv PL 4 oe

ALG: the algorithm to use. Either min-max or player inputs.
MM: minimax
PL: for player

D: depth of the search tree (recommended to not go past 6)

EVAL: evaluation function of the board. max nodes seek to maximize value of board, while min nodes seek to minimize the value of the board.
wv: weighted value
oe: Combination value
hc: hardcode value

NOTE: when playing as a player, the Depth and evaluation parameters do not matter, but still need parameters. Additionally, the game will not stop if the player wins. Additionally, there are no safeguards in place for the player, so only input legal commands.
