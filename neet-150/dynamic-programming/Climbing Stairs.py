class Solution:
    # Recursion
    def climbStairs1(self, n: int) -> int:

        def dfs(i):
            if i > n:
                return 0
            elif i == n:
                return 1

            return dfs(i + 1) + dfs(i + 2)

        return dfs(0)

    # Top Down
    def climbStairs2(self, n: int) -> int:
        memo = {n + 1: 0, n: 1}

        def dfs(i):
            if i in memo:
                return memo[i]

            memo[i] = dfs(i + 1) + dfs(i + 2)
            return memo[i]

        return dfs(0)

    # Bottom Up
    def climbStairs3(self, n: int) -> int:
        if n < 2:
            return n
        # [0,0,0,0,...]
        memo = [0] * n

        # [1,2,0,0,...]
        memo[0], memo[1] = 1, 2

        for i in range(2, n):
            memo[i] = memo[i - 1] + memo[i - 2]
        return memo[n - 1]

    # Space Optimized
    def climbStairs4(self, n: int) -> int:
        # [x, x, x, x, ...] 1, 0
        one, two = 1, 0

        for _ in range(n - 1, -1, -1):
            print(_)
            temp = one + two
            two = one
            one = temp

        return one


solutions = Solution()
res = solutions.climbStairs3(2)
print(res)
