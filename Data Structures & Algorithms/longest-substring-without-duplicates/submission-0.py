class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0 
        L = 0

        # hash set to store unique substring
        sub = set()
        
        # sliding window of L to R
        for R in range(len(s)):
            if s[R] in sub:
                # Shrink window L until s[R] gets removed
                while s[R] in sub:
                    sub.remove(s[L])
                    L += 1

            # add next character to the right
            sub.add(s[R])
            length = max(length, len(sub))

        return length
