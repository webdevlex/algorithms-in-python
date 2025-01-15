from typing import List


class Solution:
    # Brute Force
    def rob1(self, nums: List[int]) -> int:
        def dfs(i):
            if i >= len(nums):
                return 0
            return max(nums[i] + dfs(i + 2), dfs(i + 1))

        return dfs(0)

    # Top Down
    def rob2(self, nums: List[int]) -> int:
        memo = {len(nums): 0, len(nums) + 1: 0}

        def dfs(i):
            if i in memo:
                return memo[i]

            memo[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
            return memo[i]

        return dfs(0)

    # Bottom Up
    def rob3(self, nums: List[int]) -> int:
        memo = [0] * (len(nums) + 2)

        for i in range(len(nums) - 1, -1, -1):
            memo[i] = max(nums[i] + memo[i + 2], memo[i + 1])

        return memo[0]

    # Space optimized
    def rob4(self, nums: List[int]) -> int:
        left, right = 0, 0

        for i in range(len(nums) - 1, -1, -1):
            temp = left
            left = max(nums[i] + right, left)
            right = temp

        return left


solutions = Solution()
res = solutions.rob4([1, 1, 3, 3])

print(res)
