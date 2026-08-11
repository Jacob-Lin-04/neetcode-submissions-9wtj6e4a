class TrieNode:
    def __init__(self):
        # Dictionary maps char to TrieNode
        self.children = {}
        self.word = False

class PrefixTree:

    def __init__(self):
        # Intilize empty root node
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        # Go through every character in word
        for c in word:
            if c not in curr.children:
                # Insert trie node if not already in children
                curr.children[c] = TrieNode()

            curr = curr.children[c]
        
        # Indicate end of word if it is last character
        curr.word = True


    def search(self, word: str) -> bool:
        curr = self.root

        # Go through every character in word
        for c in word:
            if c not in curr.children:
                # If the character does not exist 
                # Word cannot exist
                return False
            
            curr = curr.children[c]
        
        # Return if this character is end of word
        return curr.word


    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        # Iteratete through prefix
        for c in prefix:
            if c not in curr.children:
                return False

            curr = curr.children[c]
        
        return True


        
        