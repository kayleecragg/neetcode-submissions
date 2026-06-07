class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            queue = deque()
            visit.add((r, c))
            queue.append((r, c))

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    hi, bye = row + dr, col + dc
                    if (hi in range(ROWS)) and (bye in range(COLS)) and grid[hi][bye] == "1" and (hi, bye) not in visit:
                        queue.append((hi, bye))
                        visit.add((hi, bye))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        return islands


        