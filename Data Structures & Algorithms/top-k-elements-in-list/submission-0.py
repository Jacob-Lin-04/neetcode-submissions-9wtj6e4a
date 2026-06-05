import collections
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        
        for num in nums:
            #0 if key doesnt exist yet
            freq[num] = freq.get(num, 0) + 1

        # finds k number of keys with largest values 
        top_k = heapq.nlargest(k, freq.keys(), key=lambda x: freq[x])

        #return topk keys
        return top_k
        

        