class Solution:
    # Recursion
    # Time Complexity: O(2^n)
    # Space Complexity: O(n)
    def climbStairs1(self, n: int) -> int:
        def dfs(steps):
            if steps == n:
                return 1
            elif steps > n:
                return 0
            return dfs(steps + 1) + dfs(steps + 2)

        return dfs(0)

    # Top Down
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def climbStairs2(self, n: int) -> int:
        memo = {n: 1, n + 1: 0}

        def dfs(steps):
            if steps in memo:
                return memo[steps]

            memo[steps] = dfs(steps + 1) + dfs(steps + 2)
            return memo[steps]

        return dfs(0)

    # Bottom Up
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def climbStairs3(self, n: int) -> int:
        memo = {n: 1, n + 1: 0}

        for i in range(n - 1, -1, -1):
            memo[i] = memo[i + 1] + memo[i + 2]

        return memo[0]

    # Space Optimized
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def climbStairs4(self, n: int) -> int:
        left, right = 1, 0

        for _ in range(n - 1, -1, -1):
            temp = left
            left = left + right
            right = temp

        return left


solutions = Solution()
res = solutions.climbStairs3(3)
print(res)
