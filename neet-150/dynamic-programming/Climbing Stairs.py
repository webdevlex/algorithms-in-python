# Recursion
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {0: 1, 1: 1}

        def helper(n):
            if n in memo:
                return memo[n]

            memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
            return memo[n]

        return helper(n)


# Space optimized
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for _ in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one
