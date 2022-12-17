class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
                
            node = node.children[char]
            
        node.isEnd = True
        
    def find(self):
        
        def dfs(directory, node):
            if node.isEnd:
                res.append('/' + '/'.join(directory))
                return 
            
            for char in node.children:
                dfs(directory + [char], node.children[char])
                
        res = []
        dfs([], self.root)
        return res
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        t = Trie()
        
        for f in folder:
            f = f.split('/')[1:]
            t.insert(f)
            
        return t.find()
        