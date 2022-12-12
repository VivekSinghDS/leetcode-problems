class Solution:
    def oddString(self, words: List[str]) -> str:
        
        store = defaultdict(list)
        flag = False 

        for word in words:
            arr = []
            for i in range(1, len(word)):
                # print(word[i], word[i - 1])
                a = ord(word[i]) - ord("a")
                b = ord(word[i - 1]) - ord('a')
                
                arr.append(a - b)
                

                
            store[tuple(arr)].append(word)
        
        # print(store)
        for arr in store:
            if len(store[arr])==1:
                return store[arr][0]

            
    
                
                
                
                
        
        