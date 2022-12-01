class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        counter_first = 0
        counter_second = 0
        
        for i in range(int(len(s) / 2)):
            if s[i] in 'aeiou':
                counter_first += 1
            
        for i in range(int(len(s) / 2), len(s)):
            if s[i] in "aeiou":
                counter_second += 1
        
        # print(counter_first, counter_second)
        return counter_first == counter_second
        