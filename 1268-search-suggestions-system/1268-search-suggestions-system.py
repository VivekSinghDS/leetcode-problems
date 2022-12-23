class Node:
    def __init__(self):
        self.children = {}
        self.suggestions = []
        
class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self, word):
        cur = self.root 
        
        for char in word:
            if char not in cur.children:
                cur.children[char] = Node()
                
            if len(cur.suggestions) < 3:
                cur.suggestions.append(word)
                
            cur = cur.children[char]    
            
        if len(cur.suggestions) < 3:
            cur.suggestions.append(word)
            
    def find(self, word):
        cur = self.root 
        res = []
        for char in word:
            if char not in cur.children:
                break 
                
            res.append(cur.children[char].suggestions)
            cur = cur.children[char]
         
        remaining = 0 
        if len(res) != len(word):
            remaining = len(word) - len(res)
            
        for i in range(remaining):
            res.append([])
            
        return res
        

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        t = Trie()
        products.sort()
        
        for product in products:
            t.insert(product)
            
        input_string = ""
        for char in searchWord:
            input_string += char
            
        return t.find(searchWord)
            
            
            
        