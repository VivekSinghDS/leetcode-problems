class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        
        val = counter.values()
        val = [-x for x in val]
        heapify(val)
        res = []
        # print(val)
        while k != 0:
            
            cur_max = -1 * heapq.heappop(val)
            
            
            for key in counter:
                if counter[key] == cur_max and key not in res:
                    res.append(key)
                    break
                    
            k -= 1
            
        return res
            
        