class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # memoisation

        # rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        # cache = [[-1] * cols for i in range(rows)]
        
        # def memoi(r, c):

        #     # base cases

        #     # if too big (out of bounds)
        #     if r == rows or c == cols:
        #         return 0
            
        #     # if it's blocked (value 1)
        #     if obstacleGrid[r][c] == 1:
        #         return 0
            
        #     # if it's already in the cache
        #     if cache[r][c] != -1:
        #         return cache[r][c]

        #     # success? if it gets to destination
        #     if r == rows -1 and c == cols -1:
        #         return 1
            
        #     cache[r][c] = (memoi(r + 1, c)) + (memoi(r, c + 1))
        #     return cache[r][c]
        
        # return(memoi(0, 0))

        # bottom up

        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [0] * n
        dp[n - 1] = 1

        for r in reversed(range(m)):
            for c in reversed(range(n)):

                if obstacleGrid[r][c]:
                    dp[c] = 0
                
                elif c + 1 < n:
                    # adding tile below it to tile to its right
                    dp[c] = dp[c] + dp[c+1]

        return dp[0]