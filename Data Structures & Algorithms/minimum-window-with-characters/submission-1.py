from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # min length of window
        min_len = float('inf')
        result = ""

        # Frequency map of characters using collections.Counter
        t_counts = Counter(t)
        # Frequency of characters in current window
        window_counts = Counter()

        # Number of unique characters in t that have the required frequency in our window
        # When have == len(t_counts), we have a valid window
        have = 0

        L = 0
        # Dynamic Sliding window, expan window by moving right pointer
        for R in range(len(s)):
            # Get char at right pointer
            char = s[R]
            
            # Add to window freq map
            window_counts[char] += 1

            # If this char is in t and we have reached required frequency for any char in t
            if char in t_counts and window_counts[char] == t_counts[char]:
                have += 1

            # Try to shrink window from left while it is still valid
            # A valid window will have all characters from t with req freq
            while have == len(t_counts):
                # Update result if current window is smaller than prev min
                if (R - L + 1) < min_len:
                    # Store substring from L to R inclusive
                    result = s[L:R+1]
                    min_len = len(result)
                
                # Get character at the left pointer
                char_l = s[L]
                
                # If removing this left character breaks our required frequency for any char in t
                if char_l in t_counts and window_counts[char_l] == t_counts[char_l]:
                    # Decrement have since the freq for said char is no longer correct
                    have -= 1
                
                # Remove the left character from windo freq map
                window_counts[char_l] -= 1
                # Move left pointer right to shrink the window
                L += 1
                
        # Returns shortest substring found or empty if none exist
        return result
