class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_map = {}

        for n in nums:
            num_map[n] = True

        return len(num_map) != len(nums)