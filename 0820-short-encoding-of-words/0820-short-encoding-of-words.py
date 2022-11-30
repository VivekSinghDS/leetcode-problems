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
        t = Trie()
        words = list(set(words))
        total = 0 
        for word in words:
            t.insert(word[::-1])
        # print(t.ends)
        for node, depth in t.ends:
            if len(node.children) == 0:
                total += depth
                
        return total
        