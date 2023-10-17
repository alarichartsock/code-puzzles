class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        i, j = len(matrix), len(matrix[0])
        left, right = 0, i * j - 1

        while left <= right:
            idx = (left + right) // 2
            mid = matrix[idx // j][idx % j]  # Convert to row, col
            
            if mid == target:
                return True
            elif mid < target:
                left = idx+ 1
            else:
                right = idx- 1
        
        return False