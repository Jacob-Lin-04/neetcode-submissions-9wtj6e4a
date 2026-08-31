class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0 
        L = 0

        # hash set to store unique substring
        sub = dict()
        
        # optimized sliding window of L to R
        for R in range(len(s)):
            if s[R] in sub and sub[s[R]] >= L:
                # Jump L directly past duplicate
                L = sub[s[R]] + 1
            
            # add next character to the right
            sub[s[R]] = R
            length = max(length, R - L + 1)

        return length
