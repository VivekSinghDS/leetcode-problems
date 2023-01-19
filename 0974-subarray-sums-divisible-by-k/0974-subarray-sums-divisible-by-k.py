class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        total = 0
        ans = 0
        mapper = defaultdict(int)
        mapper[0] += 1
        for i in range(len(nums)):
            total += nums[i]
            remainder = total % k
            if remainder < 0:
                remainder = remainder + k
            
            
            ans += mapper[remainder]
            mapper[remainder] += 1
            
                    
        return ans
                
                
        