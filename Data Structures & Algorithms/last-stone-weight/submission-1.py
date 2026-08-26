import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Use python heapq and make it max heapq
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        # While we still have more than 1 stone in th eheap
        while len(max_heap) > 1:
            s1 = heapq.heappop(max_heap)
            s2 = heapq.heappop(max_heap)

            if s1 != s2:
                # Since weights are negative we use stone 1 - stone 2 (negative difference)
                heapq.heappush(max_heap, s1 - s2)
        
        if len(max_heap) == 0:
            return 0
            
        else:
            return -1 * heapq.heappop(max_heap)

