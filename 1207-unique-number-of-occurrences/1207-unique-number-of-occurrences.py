class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        mapper = {} # value, count
        
        for n in arr:
            mapper[n] = 1 + mapper.get(n, 0)
            
        return len(set(mapper.values())) == len(mapper.values())
        