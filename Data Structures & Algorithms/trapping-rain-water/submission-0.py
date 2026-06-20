class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) -1
        water_max = 0
        left_max = 0
        right_max = 0

        while l < r:
            # if left 
            if height[l] < height[r]:
                left_max = max(height[l], left_max)
                water_max += left_max-height[l]
                l += 1

            else:
                right_max = max(height[r], right_max)
                water_max += right_max-height[r]
                r -= 1

        return water_max
            


