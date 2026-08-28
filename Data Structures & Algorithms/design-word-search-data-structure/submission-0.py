class TrieNode:
    def __init__(self):
        self.children = {} # Maps character to child TrieNode
        self.word = False # Marks end of a valid word
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
  

    def addWord(self, word: str) -> None:
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            
            cur = cur.children[c]
        
        cur.word = True # Mark end of word
        

    def search(self, word: str) -> bool:
        #Use DFS to search

        def dfs(index, node):
            # Base Case: Reached the end of the word
            
            if index == len(word):
                return node.word
            
            char = word[index]

            if char == ".":
                # Attempt to match with any child
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
                
                return False
            
            else:
                # Must match exact character

                if char not in node.children:
                    return False

                return dfs(index + 1, node.children[char])

                
        return dfs(0, self.root)
