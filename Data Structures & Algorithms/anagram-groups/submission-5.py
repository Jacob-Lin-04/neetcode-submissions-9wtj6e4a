class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # mapping character count to list of anagrams
        result = defaultdict(list)

        for s in strs:
            count = [0] * 26 # a -> z alphabet

            for c in s:
                count[ord(c) - ord("a")] += 1 # map to 0-25 and count

            #tuple is non mutable. List cannot be a key
            result[tuple(count)].append(s)

        return list(result.values())
        
        #optimal O(m* n) Solution
