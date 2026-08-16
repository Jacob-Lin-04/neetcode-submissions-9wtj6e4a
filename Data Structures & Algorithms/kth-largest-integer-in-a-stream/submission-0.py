import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # insert all numbers from nums into min heap
        self.minHeap, self.k = nums, k
        
        heapq.heapify(self.minHeap)

        # If heap size becomes greater than k
        # Continually remove the smallest element
        # Heap contains exactly k elements
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)


    def add(self, val: int) -> int:
        # Insert the new value into the min heap
        heapq.heappush(self.minHeap, val)
        
        # If heap size becomes larger than k
        # Remove the smallest element (root)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        # Return heap smallest element (kth Largest)
        return self.minHeap[0]
        
