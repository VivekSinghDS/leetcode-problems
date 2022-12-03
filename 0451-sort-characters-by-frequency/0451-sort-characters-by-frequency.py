class Solution:
    def frequencySort(self, s: str) -> str:
        freq_bucket = [[] for i in range(len(s) + 1)]
        
        counter = Counter(s)
        
        for key in counter:
            freq_bucket[counter[key]].append(key)
            
        
        res = ""
        
        for i in range(len(s), -1, -1):
            # print(i)
            if freq_bucket[i]:
                for n in freq_bucket[i]:
                    for x in range(i):
                        res += n
                    
        return res
        