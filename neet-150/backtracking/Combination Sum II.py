class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def helper(i, cur, cur_sum):
            if cur_sum == target:
                res.append(cur.copy())
                return
            elif cur_sum > target or i == len(nums):
                return

            cur.append(nums[i])
            helper(i + 1, cur, cur_sum + nums[i])
            cur.pop()
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            helper(i + 1, cur, cur_sum)

        nums.sort()
        helper(0, [], 0)
        return res
