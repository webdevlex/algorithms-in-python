from collections import deque
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        maxArea = 0
        rows, columns = len(grid), len(grid[0])

        def bfs(r, c):
            area = 1
            que = deque()
            que.append((r, c))
            grid[r][c] = -1

            while que:
                r, c = que.popleft()
                variations = [[-1, 0], [0, 1], [1, 0], [0, -1]]
                for vr, vc in variations:
                    cr, cc = r + vr, c + vc
                    if cr in range(rows) and cc in range(columns) and grid[cr][cc] == 1:
                        que.append((cr, cc))
                        grid[cr][cc] = -1
                        area += 1

            return area

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, bfs(r, c))

        return maxArea
