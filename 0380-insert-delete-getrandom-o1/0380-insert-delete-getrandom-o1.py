class RandomizedSet:

    def __init__(self):
        self.mapper = {}
        self.nums = []
        

    def insert(self, val: int) -> bool:
        if val in self.mapper:
            return False
        
        length = len(self.nums)
        self.mapper[val] = length
        self.nums.append(val)
        return True
        
        

    def remove(self, val: int) -> bool:
        if val not in self.mapper:
            return False
        last_element, idx = self.nums[-1], self.mapper[val]
        self.nums[idx], self.mapper[last_element] = last_element, idx
        
        self.nums.pop()
        del self.mapper[val]
        return True
        
        

    def getRandom(self) -> int:
        return random.choice(self.nums)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()