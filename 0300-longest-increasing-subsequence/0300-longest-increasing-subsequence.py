class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        
        for n in nums:
            i = bisect_left(sub, n)
            
            if i == len(sub):
                sub.append(n)
                
            else:
                sub[i] = n
                
        return len(sub)
        