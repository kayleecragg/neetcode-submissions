class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # memoisation

        def memoi(r, c, rows, cols, cache):

            # base cases

            # if too big (out of bounds)
            if r == rows or c == cols:
                return 0
            
            # if it's blocked (value 1)
            if obstacleGrid[r][c] == 1:
                return 0
            
            # if it's already in the cache
            if cache[r][c] > 0:
                return cache[r][c]

            # success? if it gets to destination
            if r == rows -1 and c == cols -1:
                return 1
            
            cache[r][c] = (memoi(r + 1, c, rows, cols, cache)) + (memoi(r, c + 1, rows, cols, cache))
            return cache[r][c]
        
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])

        cache = [[0] * cols for i in range(rows)]
        
        return(memoi(0, 0, rows, cols, cache))

