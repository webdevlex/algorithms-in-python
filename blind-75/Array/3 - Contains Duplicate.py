class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsDict = {}
        for num in nums:
            if num in numsDict:
                return True
            numsDict[num] = 1
        return False
