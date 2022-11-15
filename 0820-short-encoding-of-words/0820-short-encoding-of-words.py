class Node:
    def __init__(self):
        self.children = {}
        
class Trie:
    def __init__(self):
        self.root = Node()
        self.ends = []
        
    def insert(self, word):
        cur = self.root
        
        for char in word:
            if char not in cur.children:
                cur.children[char] = Node()
                
            cur = cur.children[char]
            
        self.ends.append((cur, len(word) + 1))
                
            
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = list(set(words))
        t = Trie()
        for word in words:
            t.insert(word[::-1])
        
        total = 0
        for node, depth in t.ends:
            # print(node.children)
            if len(node.children) == 0:
                
                total += depth
                
        return total
            
        
        