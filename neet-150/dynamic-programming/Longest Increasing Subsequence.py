from typing import List


class Solution:
    def lengthOfLIS1(self, nums: List[int]) -> int:
        def dfs(i):
            if i >= len(nums):
                return 0

            maxLength = 0
            for j in range(i, len(nums)):
                if nums[j] > nums[i]:
                    curLength = dfs(j)
                    if curLength > maxLength:
                        maxLength = curLength

            return maxLength + 1

        maxLength = 0
        for i in range(len(nums)):
            curLength = dfs(i)
            if curLength > maxLength:
                maxLength = curLength

        return maxLength

    def lengthOfLIS2(self, nums: List[int]) -> int:

        def dfs(i, j):
            if i == len(nums):
                return 0

            LIS = dfs(i + 1, j)  # Do not include current element

            prev = nums[j]
            curr = nums[i]
            if j == -1 or prev < curr:
                LIS = max(LIS, 1 + dfs(i + 1, i))  # include current element

            return LIS

        return dfs(0, -1)


solution = Solution()
res = solution.lengthOfLIS([9, 1, 4, 2, 3, 3, 7])
print(res)
