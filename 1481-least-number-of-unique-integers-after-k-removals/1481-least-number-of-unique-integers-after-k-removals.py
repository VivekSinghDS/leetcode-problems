class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        buckets = [[] for _ in range(len(arr) + 1)]
        counter = collections.Counter(arr)
        for key, count in counter.items():
            buckets[count].append(key)
        for count in range(len(arr) + 1):
            if k == 0: break
            while buckets[count] and k >= count:
                del counter[buckets[count].pop()]
                k -= count
        return len(counter)
        
        
            
        
        