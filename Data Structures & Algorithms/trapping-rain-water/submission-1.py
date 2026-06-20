class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) -1
        water_max = 0
        left_max = 0
        right_max = 0

        while l < r:
            # process side with smaller boundary
            if height[l] < height[r]:
                # Update leftMax with current bar height
                left_max = max(height[l], left_max)
                # Water at position l = (water level) - (bar height)
                # Water level is limited by leftMax on this side
                water_max += left_max-height[l]
                #move pointer inward
                l += 1

            else:
                # Update rightMax with current bar height
                right_max = max(height[r], right_max)
                # Water at position r = (water level) - (bar height)
                # Water level is limited by rithtMax on this side
                water_max += right_max-height[r]
                r -= 1

        return water_max
            


