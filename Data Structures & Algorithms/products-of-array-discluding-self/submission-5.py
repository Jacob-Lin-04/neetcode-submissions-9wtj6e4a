class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        #all elemtns in output array intilized to 1
        product = [1] * n 

        #compute all products before index i
        prefix = 1
        for i in range(n):
            #product of elements before I
            product[i] = prefix 
            #update prefix for next index
            prefix *= nums[i]

        #compute all products after index I
        suffix = 1
        for i in range(n - 1, -1, -1):
            #multiply by product of elements after i
            product[i] *= suffix
            #update suffex for next index to left
            suffix *= nums[i]

        return product