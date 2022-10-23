class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def helper(string, memo):
            if len(string) == 0:
                return [[]]
            
            if len(string) == 1:
                return [[string]]
            
            if string in memo:
                return memo[string]
            
            
            
            result = []
            for i in range(1, len(string) + 1):
                candidate = string[:i]
                
                if candidate == candidate[::-1]:
                    for partition in helper(string[i:], memo):
                        result.append([candidate] + partition)
                        
            memo[string] = result
            return result
        
        return helper(s, {})
                
        