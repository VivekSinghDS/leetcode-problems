class Node:
    def __init__(self):
        self.children = {}
        self.suggestions = []
        
class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self, word):
        cur = self.root    
        for character in word:
            if character not in cur.children:
                cur.children[character] = Node()
                
            if len(cur.suggestions) < 3:
                cur.suggestions.append(word)
                
            cur = cur.children[character]
        
        if len(cur.suggestions) < 3:
            cur.suggestions.append(word)

        
    def find(self, search_text):
        res = []
        cur = self.root
        string_input = ""
        
        for char in search_text:
            if char in cur.children:
                cur = cur.children[char]
                res.append(cur.suggestions)
                
            else:
                break
                
        remaining = len(search_text) - len(res)
        for j in range(remaining):
            res.append([])
        return res
        
        
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        t = Trie()
        
        for product in products:
            t.insert(product)
            
        return t.find(searchWord)