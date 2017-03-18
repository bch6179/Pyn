leetcode.com/problems/surrounded-regions/?tab=description

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X


hase 1: "Save" every O-region touching the border, changing its cells to 'S'.
Phase 2: Change every 'S' on the board to 'O' and everything else to 'X'.

def solve(self, board):
    if not any(board): return

    m, n = len(board), len(board[0])
    save = [ij for k in range(m+n) for ij in ((0, k), (m-1, k), (k, 0), (k, n-1))]
    while save:
        i, j = save.pop()
        if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
            board[i][j] = 'S'
            save += (i, j-1), (i, j+1), (i-1, j), (i+1, j)

    board[:] = [['XO'[c == 'S'] for c in row] for row in board]
In case you don't like my last line, you could do this instead:

    for row in board:
        for i, c in enumerate(row):
            row[i] = 'XO'[c == 'S']