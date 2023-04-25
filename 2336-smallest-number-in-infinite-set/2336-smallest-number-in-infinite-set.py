class SmallestInfiniteSet:

    def __init__(self):
        self.smallest_val = 1
        self.lookup = set()
        self.numbers = []
        

    def popSmallest(self) -> int:
        if self.numbers:
            value = heapq.heappop(self.numbers)
            if value in self.lookup:
                self.lookup.remove(value)
            return value 
        else:
            value = self.smallest_val 
            self.smallest_val += 1
            return value
        

    def addBack(self, num: int) -> None:
        if self.smallest_val <= num or num in self.lookup:
            return 
        
        self.lookup.add(num)
        heapq.heappush(self.numbers, num)
            
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)