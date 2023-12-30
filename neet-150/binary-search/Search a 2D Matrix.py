from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowLeft = 0
        rowRight = len(matrix) - 1

        colLeft = 0
        colRight = len(matrix[0]) - 1

        row = None
        while rowLeft <= rowRight and row is None:
            rowMid = (rowLeft + rowRight) // 2
            if matrix[rowMid][colLeft] <= target and target <= matrix[rowMid][colRight]:
                row = rowMid
            elif target < matrix[rowMid][colLeft]:
                rowRight = rowMid - 1
            else:
                rowLeft = rowMid + 1
        
        while colLeft <= colRight and row is not None:
            colMid = (colLeft + colRight) // 2
            if matrix[row][colMid] == target:
                return True
            elif matrix[row][colMid] < target:
                colLeft = colMid + 1
            else:
                colRight = colMid - 1
        return False
    
nums = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
solution = Solution()
result = solution.searchMatrix(nums, 3)
print(result)