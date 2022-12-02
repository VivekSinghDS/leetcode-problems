class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        def get_bucket(word):
            freq_word = [[] for i in range(len(word) + 1)]
            counter = Counter(word)
            for key in counter:
                freq_word[counter[key]].append(key)
                
            return freq_word, set(counter.keys())
                
            
        word1_bucket, word1_set = get_bucket(word1)
        word2_bucket, word2_set = get_bucket(word2)
        # print(word1_bucket, word2_bucket)
        if len(word1_bucket) != len(word2_bucket) or word1_set != word2_set:
            return False
        
        for i in range(len(word1)):
            if len(word1_bucket[i]) != len(word2_bucket[i]):
                return False
            
        return True
        
        
        
        
        