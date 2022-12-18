class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class Trie:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        cur = self.root
        
        for char in word:
            if char not in cur.children:
                cur.children[char] = Node()
                
            cur = cur.children[char]
            
        cur.isEnd = True 
        

    def search(self, word: str) -> bool:
        cur = self.root 
        
        for char in word:
            if char not in cur.children:
                return False 
            cur = cur.children[char]
            
        return cur.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root 
        
        for character in prefix:
            if character not in cur.children:
                return False 
            
            cur = cur.children[character]
            
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)