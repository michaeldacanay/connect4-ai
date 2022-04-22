# connect4-ai
Connect 4 is a two-player game in which players alternately place pieces on a vertical board. The player that first connects four pieces in a row wins. The board has 6 rows and 7 columns.

format: ```python connect4.py <ALG1> <D1> <EVAL1> <ALG2> <D2> <EVAL2>```

ALG: MM (minimax) or AB (alpha-beta)  
D: depth of the search tree
EVAL: evaluation function of the board. max nodes seek to maximize value of board, while min nodes seek to minimize the value of the board.
