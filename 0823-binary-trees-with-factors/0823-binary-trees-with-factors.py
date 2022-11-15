class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        ways = defaultdict(int)
        
        for a in arr:
            temp = 1
            
            for b in arr:
                if b > a:
                    break 
                
                temp += (ways[b] * ways[a / b])
                
            ways[a] = temp
            # ways[a] %= (10 ** 9 + 7)
            
        return sum(ways.values()) % (10 ** 9 + 7)
                    
                
                
        