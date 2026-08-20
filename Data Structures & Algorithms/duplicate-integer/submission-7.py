class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        r = set()
        for i in range(len(nums)):
            r.add(nums[i])
        return len(r) < len(nums)