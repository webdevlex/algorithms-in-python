from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        
        k = None
        while left <= right:
            k = (left + right)//2

            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            
            if hours == h:
                break
            elif hours < h:
                right = k - 1
            else:
                left = k + 1
        return k
            


solution = Solution()

arr = [312884470]
h = 312884469
res = solution.minEatingSpeed(arr, h)
print(res)