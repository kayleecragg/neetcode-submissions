class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        islands = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        maxCount = 0
        count = 0

        def bfs(r, c):
            queue = deque()
            visit.add((r, c))
            queue.append((r, c))
            anothercount = 1

            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    hi, bye = row + dr, col + dc
                    if (0 <= hi < ROWS) and (0 <= bye < COLS) and grid[hi][bye] == 1 and (hi, bye) not in visit:
                        anothercount += 1
                        queue.append((hi, bye))
                        visit.add((hi, bye))

            return anothercount

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visit:
                    count = bfs(r, c)
                    maxCount = max(maxCount, count)
                    islands += 1
        
        return maxCount