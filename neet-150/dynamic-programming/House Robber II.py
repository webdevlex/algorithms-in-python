from typing import List


class Solution:
    # Brute Force
    def rob1(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def dfs(i, last):
            if i >= last:
                return 0
            return max(nums[i] + dfs(i + 2, last), dfs(i + 1, last))

        return max(dfs(0, len(nums) - 1), dfs(1, len(nums)))

    # Top Down
    def rob2(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def dfs(i, memo):
            if i in memo:
                return memo[i]

            memo[i] = max(nums[i] + dfs(i + 2, memo), dfs(i + 1, memo))
            return memo[i]

        memo1 = {len(nums) - 1: 0, len(nums): 0}
        memo2 = {len(nums): 0, len(nums) + 1: 0}
        return max(dfs(0, memo1), dfs(1, memo2))

    # Bottom Up
    def rob3(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        memo1 = [0] * (len(nums) + 1)
        for i in range(len(nums) - 2, -1, -1):
            memo1[i] = max(nums[i] + memo1[i + 2], memo1[i + 1])

        memo2 = [0] * (len(nums) + 2)
        for i in range(len(nums) - 1, 0, -1):
            memo2[i] = max(nums[i] + memo2[i + 2], memo2[i + 1])

        return max(memo1[0], memo2[1])

    # Space optimized
    def rob4(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left1, right1 = 0, 0
        for i in range(len(nums) - 2, -1, -1):
            temp = left1
            left1 = max(nums[i] + right1, left1)
            right1 = temp

        left2, right2 = 0, 0
        for i in range(len(nums) - 1, 0, -1):
            temp = left2
            left2 = max(nums[i] + right2, left2)
            right2 = temp

        return max(left1, left2)


solutions = Solution()
res = solutions.rob4([1, 1, 3, 3])

print(res)
