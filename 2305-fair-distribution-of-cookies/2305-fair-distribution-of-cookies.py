class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        res = float('inf')
        count = [0]*k
        def backtrack(index):
            nonlocal res, count
            if index == len(cookies):
                res = min(max(count), res)
                return 
            
            if res <= max(count):
                return 
            
            for j in range(k):
                count[j] += cookies[index]
                backtrack(index + 1)
                count[j] -= cookies[index]
            
        backtrack(0)
        return res
        