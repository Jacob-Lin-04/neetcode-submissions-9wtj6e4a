class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                return abs(nums[i])
            else:
                # mark as visited by targetting index to current number 
                nums[index] *= -1

        return -1