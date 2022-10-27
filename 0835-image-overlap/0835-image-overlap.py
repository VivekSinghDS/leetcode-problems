class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        
        n = len(A)
        
        a1 = [(i, j) for i in range(n) for j in range(n) if A[i][j]]
        b1 = [(i, j) for i in range(n) for j in range(n) if B[i][j]]
        # print(a1, b1)
        counter = Counter((xa - xb, ya - yb) for xa, ya in a1 for xb, yb in b1)
        # print(counter)
        
        return max(counter.values() or [0])
        
        '''
        N = len(img1)
        
        def helper(x_shift, y_shift):
            num = 0 
            
            for r in range(N):
                for c in range(N):
                    if (0 <= r + y_shift < N and 0 <= c + x_shift < N and img1[r + y_shift][c + x_shift] == 1 and 
                        img2[r][c] == 1):
                        num += 1
                        
            return num 
        
        max_num = [helper(x, y) for x in range(-N, N) for y in range(-N, N)]

        return max(max_num)
            
        '''
        
        