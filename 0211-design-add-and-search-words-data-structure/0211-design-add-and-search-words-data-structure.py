class WordDictionary:

    def __init__(self):
        self.finder = defaultdict(set)
        

    def addWord(self, word: str) -> None:
        self.finder[len(word)].add(word)
        

    def search(self, word: str) -> bool:
        if "." not in word:
            return word in self.finder[len(word)]
        
        else:
            for comparer in self.finder[len(word)]:
                for i, char in enumerate(word):
                    if char != "." and comparer[i] != char:
                        break
                    
                else:
                    return True
                
            return False
                    
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)