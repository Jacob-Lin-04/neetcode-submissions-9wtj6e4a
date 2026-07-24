from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Use monotonic decreasing deque (double ended queue)
        # To keep tack of potential maximums with current maxSlidingWindow 
        output = []
        # Maintain dequeue that stores indicies of elements in decreasing order of value
        q = deque() 
        l = 0

        for r in range(len(nums)):
            # Maintain decreasing order in deque
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # Remove index that slid out of window
            if q[0] < l:
                q.popleft()
            
            # First window is ready when r >= k-1
            if r >= k -1:
                output.append(nums[q[0]])
                l += 1
            
        return output