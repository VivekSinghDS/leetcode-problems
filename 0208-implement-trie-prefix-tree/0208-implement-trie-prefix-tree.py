class Node:
    def __init__(self):
        self.children = {}
        self.endOfword = False
        
class Trie:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        cur = self.root 
        
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = Node()
                
            cur = cur.children[letter]
        
        cur.endOfword = True
        

    def search(self, word: str) -> bool:
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                return False 
            
            cur = cur.children[letter]
            
        return cur.endOfword
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for letter in prefix:
            if letter not in cur.children:
                return False 
            
            cur = cur.children[letter]
            
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)