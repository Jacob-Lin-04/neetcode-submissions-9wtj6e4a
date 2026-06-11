import re

class Solution:
    def isPalindrome(self, s: str) -> bool:

        #remove spaces and special characters
        clean = re.sub(r'[^a-zA-Z0-9]', '', s)

        left = 0
        right = len(clean) - 1
        
        

        while left < right:
            if clean[left].lower() != clean[right].lower():
                return False
            left += 1
            right -= 1

        return True
        