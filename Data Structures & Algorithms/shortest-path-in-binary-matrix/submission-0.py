class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])

        if grid[0][0] == 1:
            return -1

        visit = set()
        queue = deque()
        queue.append((0,0))
        visit.add((0,0))

        # from top left, (0,0) to bottom right

        length = 1
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                
                # clear path base case
                # if at destination (bottom right)
                if r == ROWS - 1 and c == COLS - 1:
                    return length
                
                # instead of 4 directions (right left down up)
                # all adjacent cells of the path are 8 directionally connected
                neighbours = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

                for dr, dc in neighbours:
                    hi  = r + dr
                    bye = c + dc
                    if (min(hi, bye) < 0 or  
                        hi == ROWS or bye == COLS or 
                        (hi, bye) in visit or 
                        grid[hi][bye] == 1):
                        continue
                    
                    queue.append((hi, bye))
                    visit.add((hi, bye))
            length += 1

        return -1
        