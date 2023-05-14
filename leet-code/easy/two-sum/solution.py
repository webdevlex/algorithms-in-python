class Solution(object):
    def twoSum(self, nums, target):
        myDict = {}
        for i, num in enumerate(nums):
            if num in myDict:
                myDict[num] = [myDict[num], i]
            else:
                myDict[num] = i

            requiredNum = target - num
            if requiredNum in myDict:
                if isinstance(myDict[requiredNum], list):
                    return myDict[requiredNum]
                elif myDict[requiredNum] != i:
                    return [myDict[requiredNum], i]


mySolution = Solution()

# Example 1
input = [2, 7, 11, 15]
target = 9
output = mySolution.twoSum(input, target)
print(f"\nInput: nums = {input}, target = {target}")
print(f"Output: {output}\n")

# Example 2
input = [3, 2, 4]
target = 6
output = mySolution.twoSum(input, target)
print(f"Input: nums = {input}, target = {target}")
print(f"Output: {output}\n")

# Example 3
input = [3, 3]
target = 6
output = mySolution.twoSum(input, target)
print(f"Input: nums = {input}, target = {target}")
print(f"Output: {output}\n")
