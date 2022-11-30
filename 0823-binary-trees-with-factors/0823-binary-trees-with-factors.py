class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        mapper = defaultdict(int)
        for a in arr:
            
            temp = 1
            for b in arr:
                if b > a :
                    break
                if a % b == 0:
                    temp += (mapper[b] * mapper[a / b])
                
            mapper[a] = temp
            
        return sum(mapper.values()) % (10**9 + 7)
            
            
                    
                
                
        