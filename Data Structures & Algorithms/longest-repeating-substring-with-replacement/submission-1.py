class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = 0 
        L = 0

        counts = collections.Counter()
        # Sliding window approach: expand window with R, contract with L
        for R in range(len(s)):
            # Add the character at right pointer to frequency map
            counts[s[R]] += 1
            
            # Find the most frequent character count in the current window
            # This tells us how many characters we DON'T need to replace
            max_freq = max(counts.values())

            # Check if we have too many characters to replace
            # (R - L + 1) = window size, max_freq = chars we keep
            # So (R - L + 1) - max_freq = chars we need to replace
            # If this exceeds k, we must shrink the window
            while (R - L + 1) - max_freq > k:
                # Remove the leftmost character from our frequency map
                counts[s[L]] -= 1
                # Move left pointer right to shrink the window
                L += 1

            # Update the maximum valid window size we've found so far
            # A valid window is one where we can make all chars the same with ≤ k replacements
            length = max(length, R - L + 1)

        return length
