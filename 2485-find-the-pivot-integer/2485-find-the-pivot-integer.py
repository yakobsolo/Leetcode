class Solution:
    def pivotInteger(self, n: int) -> int:
        tot = n*(n+1)/2
        temp = 0
        if n == 1:
            return n
        for i in range(1, n):
            
            
            temp += i
            if tot == temp:
                return i
            tot -= i
        return -1
            
            
            