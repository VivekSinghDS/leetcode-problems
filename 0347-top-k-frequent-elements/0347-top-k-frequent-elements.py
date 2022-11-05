class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]
        res = []
        
        for key, val in counter.items():
            freq[val].append(key)
            
        for i in range(len(freq) - 1, -1, -1):
            for val in freq[i]:
                res.append(val)
                if k == len(res):
                    return res
                    

            
        