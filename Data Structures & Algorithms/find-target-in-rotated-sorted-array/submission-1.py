class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # solution using binary search
        L, R = 0, len(nums) -1

        while L <= R:
            mid = (L + R) // 2
            
            # Find if mid is target
            if nums[mid] == target:
                return mid

            # left side is sorted 
            if nums[L] <= nums[mid]:
                # check if target is in that range
                if nums[L] <= target < nums[mid]:
                    R = mid - 1
                else:
                    L = mid + 1

            # Else right side is sorted
            else:
                if nums[mid] < target <= nums[R]:
                    L = mid + 1
                else:
                    R = mid - 1

        # by end of loop L and R pointers will converge
        # on index of the target element
        return -1