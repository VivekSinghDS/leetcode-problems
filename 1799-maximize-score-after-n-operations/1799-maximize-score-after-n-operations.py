class Solution:
    def maxScore(self, nums: List[int]) -> int:
        cache = defaultdict(int)
        
        def dfs(mask, operation):
            if mask in cache:
                return cache[mask]
            
            for i in range(len(nums)):
                if (1 << i) & mask:
                    continue
                for j in range(i + 1, len(nums)):
                    if (1 << j) & mask:
                        continue 
                    new_mask = (1 << i) | mask | (1 << j)
                    score = operation * math.gcd(nums[i], nums[j])
                    cache[mask] = max(cache[mask], score + dfs(new_mask, operation + 1))
            return cache[mask]
        return dfs(0, 1)
                    
                    
                    
        