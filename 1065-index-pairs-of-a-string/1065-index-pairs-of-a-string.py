class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False 
        
class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self, word):
        cur = self.root 
        for character in word:
            if character not in cur.children:
                cur.children[character] = Node()
            cur = cur.children[character]
            
        cur.isEnd = True
        
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        t = Trie()
        for word in words:
            t.insert(word)
            
        res = []
        for i in range(len(text)):
            cur = t.root
            for j in range(i, len(text)):
                if text[j] not in cur.children:
                    break 
                    
                cur = cur.children[text[j]]
                if cur.isEnd:
                    res.append((i, j))
        # res.sort()
        return res
                
            
            
        