class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        count = 0
        
        for i in range(len(s)):
            if s[i] == goal[i]:
                continue 
                
            count += 1
            
        if count == 2:
            return Counter(goal) == Counter(s)
        elif count == 0:
            return not len(set(goal)) == len(goal)
        else:
            return False

            
        