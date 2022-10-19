class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        
        heap = [(-freq, word) for word, freq in counter.items()]
        
        heapq.heapify(heap)
        res = []
        while k:
            _, element = heapq.heappop(heap)
            res.append(element)
            k -= 1
            
        return res
        
        
        
        