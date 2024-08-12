from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows, columns = len(grid), len(grid[0])

        def bfs(r, c):
            que = deque()
            que.append((r, c))
            grid[r][c] = "x"

            while que:
                item = que.popleft()
                r, c = item
                variations = [[-1, 0], [0, 1], [1, 0], [0, -1]]
                for vr, vc in variations:
                    cr = r + vr
                    cc = c + vc
                    if (
                        cr in range(rows)
                        and cc in range(columns)
                        and grid[cr][cc] != "x"
                        and grid[cr][cc] != "0"
                    ):
                        grid[cr][cc] = "x"
                        que.append((cr, cc))

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1":
                    islands += 1
                    bfs(r, c)

        return islands
