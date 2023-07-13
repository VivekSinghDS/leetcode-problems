class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        res = 0
        @cache
        def dfs(index, balance):
            nonlocal res
            if index == len(requests):
                count = 0
                for b in balance:
                    if b == 0:
                        count += 1
                    else:
                        return float('-inf')
                else:
                    return 0
            
            balance_2 = list(balance)
            balance_2[requests[index][0]] -= 1
            balance_2[requests[index][1]] += 1
            
            return max(1 + dfs(index + 1, tuple(balance_2)), dfs(index + 1, balance))
        return dfs(0, tuple([0]*n))
                
                    
                    
        