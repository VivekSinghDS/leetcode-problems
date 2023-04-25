class SmallestInfiniteSet:

    def __init__(self):
        self.current = [i for i in range(1, 1001)]
        self.remove_set = set()
        heapify(self.current)

    def popSmallest(self) -> int:
        # print(self.current)
        if self.current:  
            value = heapq.heappop(self.current)
            self.remove_set.add(value)
            return value
        
        else:
            return 0
        

    def addBack(self, num: int) -> None:
        if num in self.remove_set:
            heapq.heappush(self.current, num)
            self.remove_set.remove(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)