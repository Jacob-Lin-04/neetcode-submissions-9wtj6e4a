class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # search through every row
        for i, row in enumerate(matrix):
            left = 0 
            right = len(matrix[i]) - 1
            
            # binary search through each row since it is sorted

            while left <= right:
                mid = (left + right) // 2

                if target > matrix[i][mid]:
                    left = mid + 1
                elif target < matrix[i][mid]:
                    right = mid - 1 
                else:
                    return True

        return False
