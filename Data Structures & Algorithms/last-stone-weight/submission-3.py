class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # make max heap instead of min
        max_heap = [-n for n in stones]  
        heapq.heapify(max_heap)

        if len(max_heap) == 1:
            return -max_heap[0]
         
        # Continue the simulation until 
        # there is no more than one stone remaining.
        while len(max_heap) > 1:
            y = -heapq.heappop(max_heap)
            x = -heapq.heappop(max_heap)
            if x < y:
                heapq.heappush(max_heap, -(y - x))
            
        if len(max_heap) == 0:
            return 0

        else:
            return -max_heap[0]