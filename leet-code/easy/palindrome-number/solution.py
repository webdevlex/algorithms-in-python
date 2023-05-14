class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


mySolution = Solution()

# Example 1
input = 121
output = mySolution.isPalindrome(input)
print(f"\nInput: x = {input}")
print(f"Output: {output}")

# Example 2
input = -121
output = mySolution.isPalindrome(input)
print(f"\nInput: x = {input}")
print(f"Output: {output}")

# Example 1
input = 10
output = mySolution.isPalindrome(input)
print(f"\nInput: x = {input}")
print(f"Output: {output}")
