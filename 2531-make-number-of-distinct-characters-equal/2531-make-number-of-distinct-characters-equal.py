class Solution:
    def insert_and_remove(self, counter, toInsert, toRemove):
        counter[toInsert] += 1
        counter[toRemove] -= 1
        
        if counter[toRemove] == 0:
            del counter[toRemove]
        
        
    def isItPossible(self, word1: str, word2: str) -> bool:
        w1 = defaultdict(int)
        w2 = defaultdict(int)
        
        for char in word1:
            w1[char] += 1
            
        for char in word2:
            w2[char] += 1
        
        for k1 in string.ascii_lowercase:
            for k2 in string.ascii_lowercase:
                if k1 not in w1 or k2 not in w2:
                    continue
                self.insert_and_remove(w1, k2, k1)
                self.insert_and_remove(w2, k1, k2)
                
                if len(w1) == len(w2):
                    return True
                
                self.insert_and_remove(w1, k1, k2)
                self.insert_and_remove(w2, k2, k1)
                
        return False