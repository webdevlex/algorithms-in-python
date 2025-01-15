from typing import List


class Solution:
    def coinChange1(self, coins: List[int], amount: int) -> int:
        # Brute force
        def dfs(amount):
            if amount == 0:
                return 0

            res = float("inf")
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))
            return res

        minCoins = dfs(amount)
        return -1 if minCoins >= float("inf") else minCoins

    # Top Down
    def coinChange2(self, coins: List[int], amount: int) -> int:
        memo = {0: 0}

        def dfs(amount):
            if amount in memo:
                return memo[amount]

            res = float("inf")
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))

            memo[amount] = res
            return res

        minCoins = dfs(amount)

        print(memo)
        return -1 if minCoins >= float("inf") else minCoins

    # Bottom Up
    def coinChange3(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        print(dp)
        return dp[amount] if dp[amount] != amount + 1 else -1


solution = Solution()
res = solution.coinChange3([1, 3, 4, 5], 7)
print(res)
