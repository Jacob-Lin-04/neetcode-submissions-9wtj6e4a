class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            # Map the current number to an index
            index = abs(nums[i]) - 1

            # Check if this index was already marked (-Ve value)
            if nums[index] < 0:
                # We have visited number before and its the duplicate
                return abs(nums[i])
            else:
                # mark this index as visited by multiplying by -1
                nums[index] *= -1

        return -1