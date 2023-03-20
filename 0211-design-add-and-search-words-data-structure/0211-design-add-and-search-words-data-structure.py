class WordDictionary:

    def __init__(self):
        self.mapper = defaultdict(set)
        

    def addWord(self, word: str) -> None:
        self.mapper[len(word)].add(word)
        

    def search(self, word: str) -> bool:
        if "." not in word:
            return word in self.mapper[len(word)]
        
        else:
            flag = False
            # print(word, self.mapper[len(word)])
            for reference in self.mapper[len(word)]:
                for i , char in enumerate(word):
                    if char != "." and reference[i] != char:
                        break 
                        
                else:
                    return True
                
            if not flag:
                return flag
                    
                    
                    
                    
                        
                    
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)