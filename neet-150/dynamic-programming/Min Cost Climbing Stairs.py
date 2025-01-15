from typing import List


class Solution:
    # Recusion
    # Time Complexity: O(2^n)
    # Space Complexity: O(n)
    def minCostClimbingStairs1(self, cost: List[int]) -> int:
        def dfs(n):
            if n >= len(cost):
                return 0

            return min(cost[n] + dfs(n + 1), cost[n] + dfs(n + 2))

        return min(dfs(0, 0), dfs(1, 0))

    # Top Down
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        memo = {len(cost): 0, len(cost) + 1: 0}

        def dfs(n):
            if n in memo:
                return memo[n]

            memo[n] = min(cost[n] + dfs(n + 1), cost[n] + dfs(n + 2))
            return memo[n]

        return min(dfs(0), dfs(1))

    # Bottom up
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        dp = {length: 0, length + 1: 0}

        for i in range(length - 1, -1, -1):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])

        return min(dp[0], dp[1])

    # Space optimizeds
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def minCostClimbingStairs4(self, cost: List[int]) -> int:
        left, right = 0, 0

        for i in range(len(cost) - 1, -1, -1):
            temp = left
            left = cost[i] + min(left, right)
            right = temp

        return min(left, right)


solutions = Solution()
res = solutions.minCostClimbingStairs3([1, 2, 1, 2, 1, 1, 1])

print(res)
