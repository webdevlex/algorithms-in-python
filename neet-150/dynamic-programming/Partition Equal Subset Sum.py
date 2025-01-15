from typing import List


class Solution:
    # Recursion
    # Time: O(2^n)
    # Space: O(n)
    def canPartition1(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        def dfs(i, target):
            if i >= len(nums):
                return target == 0
            if target < 0:
                return False

            return dfs(i + 1, target) or dfs(i + 1, target - nums[i])

        return dfs(0, sum(nums) // 2)

    # Dynamic Programming (Top-Down)
    # Time: O(n * target)
    # Space: O(n * target)
    def canPartition2(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        n = len(nums)
        memo = [[-1] * (target + 1) for _ in range(n + 1)]

        def dfs(i, target):
            if target == 0:
                return True
            if i >= n or target < 0:
                return False
            if memo[i][target] != -1:
                return memo[i][target]

            memo[i][target] = dfs(i + 1, target) or dfs(i + 1, target - nums[i])
            return memo[i][target]

        res = dfs(0, target)
        print(memo)
        return res

    # Dynamic Programming (Bottom-Up)
    # Time: O(n * target)
    # Space: O(n * target)
    #
    # Using all numbers up to nums[i], can I form a sum of j?
    def canPartition3(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        n = len(nums)
        dp = [[False] * (target + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if nums[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][target]

    # Dynamic Programming (Optimal)
    # Time: O(n * target)
    # Space: O(target)
    #
    # Given all the items I’ve processed so far (including the current one), can I form the sum j?
    def canPartition4(self, nums: list[int]) -> bool:
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2
        dp = [False] * (target + 1)

        dp[0] = True
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[target]


solution = Solution()
res = solution.canPartition3([1, 2, 3, 4])
print(res)
