from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        def capture(r, c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or
                    board[r][c] != "O"):
                return
            board[r][c] = "T"
            for d in directions:
                print(d)
                capture(r+d[0], c+d[1])

        for r in range(ROWS):
            if board[r][0] == "O":
                capture(r, 0)
            if board[r][COLS-1] == "O":
                capture(r, COLS-1)

        for c in range(COLS):
            if board[0][c] == "O":
                capture(0, c)
            if board[ROWS-1][c] == "O":
                capture(ROWS-1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"

        return

if __name__ == "__main__":
    sol = Solution()
    test = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    sol.solve(test)
    print(test)

