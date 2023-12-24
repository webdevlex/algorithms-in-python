from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        columns = [set() for i in range(9)]
        threes = [[set() for i in range(3)] for i in range(3)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num != ".":
                    # Handle rows
                    if num in rows[r]:
                        return False
                    rows[r].add(num)

                    # Handle columns
                    if num in columns[c]:
                        return False
                    columns[c].add(num)

                    # Handle 3 x 3
                    threeRow = r // 3
                    threeColumn = c // 3
                    if num in threes[threeRow][threeColumn]:
                        return False
                    threes[threeRow][threeColumn].add(num)
        return True
