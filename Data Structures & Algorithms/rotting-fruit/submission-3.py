class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # minutes?
        minutes = 0
        fresh = 0

        # storing all rotten fruits in a queue

        # making a queue 
        queue = deque()
        # and a visited set? 
        # im not sure we need this
        # visited = set()

        # dimensions of the grid
        ROWS, COLS = len(grid), len(grid[0]) 

        # directions to go in
        adjacent = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        # going through grid and finding all rotten fruit
        # appending them into the queue

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        
        # while queue is not empty
        while queue:
            # go through all elements in queue (rotten bananas) 
            for i in range(len(queue)): # all the current rotten bananas
                r, c = queue.popleft()

                # directions
                for dr, dc in adjacent:
                    start, end = r + dr, c + dc
                    # if in bounds
                    # and its a fresh fruit

                    if (start in range(ROWS)) and (end in range(COLS)) and grid[start][end] == 1:
                        # make it a rotten banana
                        grid[start][end] = 2
                        # append it to the queue
                        queue.append((start, end))
                        fresh -= 1
                        
            if queue:
                minutes += 1
        
        if fresh == 0:
            return minutes 
        else:
            return -1