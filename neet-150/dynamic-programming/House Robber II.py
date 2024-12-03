from typing import List


class Solution:
    # Recusion
    def rob1(self, nums: List[int]) -> int:
        def dfs(n):
            if n < 0:
                return 0

            return max(nums[n] + dfs(n - 2), dfs(n - 1))

        return dfs(len(nums) - 1)

    # Top Down
    def rob2(self, nums: List[int]) -> int:
        memo = {-1: 0, -2: 0}

        def dfs(n):
            if n in memo:
                return memo[n]

            memo[n] = max(nums[n] + dfs(n - 2), dfs(n - 1))
            return memo[n]

        return dfs(len(nums) - 1)

    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[-1]

    # Space optimizeds
    def rob4(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for num in nums:
            temp = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2


solutions = Solution()
res = solutions.rob3([0, 0, 2, 9, 8, 3, 6])

print(res)
