class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # Get Character Frequency map for s1
        s1_freq = Counter(s1)

        # Check if two substrings are permutations
        window_count = Counter(s2[:len(s1)])
        for i in range(len(s1), len(s2) + 1):
            if s1_freq == window_count:
                return True

            if i < len(s2):
                # Add new character on the right
                window_count[s2[i]] += 1
                
                # Remove character on the left
                left_char = s2[i - len(s1)]
                window_count[left_char] -= 1

                if window_count[left_char] == 0:
                    del window_count[left_char]
                    
        return False

        