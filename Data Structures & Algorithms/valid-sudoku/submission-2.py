class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check rows
        for i in range(9):
            row = [0] * 10
            for j in range(9):
                if board[i][j] == ".":
                    continue
                num = int(board[i][j])
                if row[num] == 1:
                    return False
                row[num] = 1

        # Check columns
        for j in range(9):
            col = [0] * 10
            for i in range(9):
                if board[i][j] == ".":
                    continue
                num = int(board[i][j])
                if col[num] == 1:
                    return False
                col[num] = 1

        # Check 3x3 sub-boxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box = [0] * 10
                for i in range(3):
                    for j in range(3):
                        val = board[box_row + i][box_col + j]
                        if val == ".":
                            continue
                        num = int(val)
                        if box[num] == 1:
                            return False
                        box[num] = 1

        return True
