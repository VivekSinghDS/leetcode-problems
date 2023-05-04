class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_count = senate.count("R")
        d_count = len(senate) - r_count
        flag_r, flag_d = 0, 0
        rights = [1 for i in range(len(senate))]
        total = len(senate)
        
        while not(total < 0):
            for i in range(len(senate)):
                if rights[i] == 0:
                    continue
                if r_count == 0:
                    return "Dire"
                elif d_count == 0:
                    return "Radiant"

                if senate[i] == "R":
                    if flag_r > 0:
                        rights[i] = 0
                        flag_r -= 1
                        total -= 1
                    else:
                        flag_d += 1
                        d_count -= 1     

                elif senate[i] == "D":
                    if flag_d > 0:
                        rights[i] = 0
                        flag_d -= 1
                        total -= 1
                    else:
                        flag_r += 1
                        r_count -= 1
                        
                        
        

        