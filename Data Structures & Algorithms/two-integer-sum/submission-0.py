class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #empty dict
        e = dict()
        #search through list
        for i, num in enumerate(nums):
            #value needed to achive target
            complement = target - num
            
            #check if value exists as a key
            if complement in e:
                return [e[complement], i]
            else:
                #store current value and its index for future lookup
                e[num] = i
        