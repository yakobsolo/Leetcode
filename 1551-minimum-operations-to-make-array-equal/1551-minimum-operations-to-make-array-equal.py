class Solution:
    def minOperations(self, n: int) -> int:
        if n&1 == 1:
            mid = 2*(n//2)+1
        else:
            mid = 2*n//2
        
        sm = 0
        for i in range(n//2+1):
            
            sm+=(mid -((2*i)+1))
            # print(i, mid, sm)
        if n&1==0:
            sm+=1
        return sm