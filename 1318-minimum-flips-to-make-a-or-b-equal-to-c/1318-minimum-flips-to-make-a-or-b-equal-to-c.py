class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a = str(bin(a))
        b = str(bin(b))
        c = str(bin(c))
        # print(a, b, c)
        a = a.split('0b')[1]
        b = b.split('0b')[1]
        c = c.split('0b')[1]
        
        if len(a) > len(b):
            b = "0"*(len(a) - len(b)) + b
        else:
            a = "0" *(len(b) - len(a)) + a
        
        if len(c) < len(a):
            c = "0"*(len(a) - len(c)) + c
        count = 0
        if len(c) > len(a):
            a = "0"*(len(c) - len(a)) + a
            b = "0"*(len(c) - len(b)) + b
        # print(a, b, c)
        for i, j, ans in zip(a[::-1], b[::-1], c[::-1]):
            if ans == "1":
                if str(1) in [i, j]:
                    continue 
                else:
                    # print('for c = ', ans)
                    count += 1
            
            elif ans == "0":
                # print('here')
                count += int(i) + int(j)
        return count
                
            
            
        
        