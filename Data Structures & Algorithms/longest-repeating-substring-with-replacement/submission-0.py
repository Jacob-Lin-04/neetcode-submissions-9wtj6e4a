class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = 0 
        L = 0

        counts = collections.Counter()
        # optimized sliding window of L to R
        for R in range(len(s)):
            # add right most value to count
            counts[s[R]] += 1
            
            # The most frequent character count in the current window
            max_freq = max(counts.values())

            # check if the number of other characters exceeds k
            while (R - L + 1) - max_freq > k:
                counts[s[L]] -= 1
                
                L += 1

            # update if length of new window post replacement
            # is larger than previous max
            length = max(length, R - L + 1)

        return length
