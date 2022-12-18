class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False 
        
class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self, word):
        cur = self.root
        
        for char in word:
            if char not in cur.children:
                cur.children[char] = Node()
                
            cur = cur.children[char]
            
        cur.isEnd = True 
        
    def find(self):
        def dfs(node, directory):
            if node.isEnd:
                res.append('/' + '/'.join(directory))
                return 
            
            for children in node.children:
                dfs(node.children[children], directory + [children])
                
            
        res = []
        dfs(self.root, [])
        return res
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()

        t = Trie()
        for f in folder:
            f = f.split('/')[1:]
            t.insert(f)
            
        return t.find()
            
        