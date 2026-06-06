class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for i in strs:
            encoded_string += str(len(i)) + "#" + i

        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []

        # pointer to index
        i = 0
        while i < len(s):
            #find # delimeter starting from current position
            scan = s.find('#', i)

            #extra number before delimeter and convert to length of string
            length = int(s[i:scan])

            #Jump to end of the word by by using length
            word = s[scan + 1: scan + 1 + length]
            
            #move pointer to the start of the next block/word
            i = scan + 1 + length
            
            #add word to output List
            decoded_strs.append(word)
       
        return decoded_strs
