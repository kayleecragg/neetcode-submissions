class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
       
        # if grid is invalid, just return imm
        if not grid:
            return
        
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        outsidevisited = set()

        def bfs(r, c):
            visited = set()
            queue = deque()
            queue.append((r, c))
            distancetonearesttreasurechest = 1

            while queue:
                for _ in range(len(queue)):
                    row, col = queue.popleft()
                    for dr, dc in directions:
                        hi, bye = row + dr, col + dc
                        # if in the boundaries of the grid
                        if ((0 <= hi < ROWS) and (0 <= bye < COLS) and 
                            # is NOT a treasure chest and
                            ((grid[hi][bye] != 0) 
                            # is NOT a water cell
                            and grid[hi][bye] != -1) and
                            # not in visited
                            (hi, bye) not in visited):
                            
                            
                            queue.append((hi, bye))
                            visited.add((hi, bye))
                        
                        elif ((0 <= hi < ROWS) and (0 <= bye < COLS) and
                            grid[hi][bye] == 0):
                                return distancetonearesttreasurechest
                    
                distancetonearesttreasurechest += 1
                
            return 2147483647


        # traversing through every cell inside the grid
        for r in range(ROWS):
            for c in range(COLS):
                # if the cell is a land cell
                if grid[r][c] == 2147483647:
                    distancetonearesttreasurechest = bfs(r, c)
                    # if there is a way
                    if distancetonearesttreasurechest != 2147483647:
                        grid[r][c] = distancetonearesttreasurechest