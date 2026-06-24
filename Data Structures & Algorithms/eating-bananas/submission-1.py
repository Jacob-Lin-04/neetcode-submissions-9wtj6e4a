class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #slowest eating rate to maxiumum since h > number of piles
        l, r = 1, max(piles)

        min_rate = r
        
        # in search range of rates
        while l <= r:
            #find the mid point rate
            mid = (l + r) //2

            # divide each pile by mid eatin rate and sum to compare to h
            if sum(math.ceil(p / mid) for p in piles) <= h:
                # if mid eating rate is within time save it
                min_rate = mid
                # divide search range to lower half to find potential smaller rate
                r = mid - 1
            else:
                # mid rate is too slow; bring start of search to top half
                l = mid + 1

        return min_rate


        
   



        