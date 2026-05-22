class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # given: matrix
        # given target


        rows = len(matrix)
        cols = len(matrix[0])

        low = 0
        high = (rows * cols) - 1

        while low <= high:
            mid = (low + high) // 2

            r = mid // cols
            c = mid % cols

            if target < matrix[r][c]:
                high = mid - 1
            elif target > matrix[r][c]:
                low = mid + 1
            else:
                return True
        
        return False