class Solution:
    def findMin(self, nums: List[int]) -> int:
        #brute force Solution
        min_num = 1001

        for num in nums:
            min_num= min(num, min_num)

        return min_num