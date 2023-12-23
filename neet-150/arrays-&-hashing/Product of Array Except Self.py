from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [1] * length
        pre = 1
        post = 1
        for i in range(length):
            result[i] *= pre
            result[length - i - 1] *= post

            pre *= nums[i]
            post *= nums[length - i - 1]
        return result
