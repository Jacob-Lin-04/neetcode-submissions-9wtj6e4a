class Solution:
    def findMin(self, nums: List[int]) -> int:
        # solution using binary search
        L, R = 0, len(nums) -1

        while L < R:
            mid = (L + R) // 2

            # the min value of the array must be in right half
            if nums[mid] > nums[R]:
                L = mid + 1

            # min value of the array must be at mid or left of it
            elif nums[mid] < nums[R]:
                R = mid

        return nums[L]
        






        