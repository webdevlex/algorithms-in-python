from typing import List


class Solution:
    # Recusion
    def minCostClimbingStairs1(self, cost: List[int]) -> int:
        def dfs(n):
            if n >= len(cost):
                return 0

            return cost[n] + min(dfs(n + 1), dfs(n + 2))

        return min(dfs(0), dfs(1))

    # Top Down
    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        length = len(cost)
        memo = {length: 0, length + 1: 0}

        def dfs(n):
            if n in memo:
                return memo[n]
            memo[n] = cost[n] + min(dfs(n + 1), dfs(n + 2))
            return memo[n]

        return min(dfs(0), dfs(1))

    # Bottom up
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)

        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        return dp[n]

    # Space optimizeds
    def minCostClimbingStairs4(self, cost: List[int]) -> int:
        for i in range(len(cost) - 3, -1, -1):
            cost[i] = cost[i] + min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])


solutions = Solution()
res = solutions.minCostClimbingStairs3([1, 2, 1, 2, 1, 1, 1])

print(res)
