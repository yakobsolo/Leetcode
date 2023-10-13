class Solution:
    def countOrders(self, n: int) -> int:
        res = 1
        mod  = 10**9 + 7
        k = n*2
       
        for _ in range(n*2):
            res  =(res*k)
            k-=1
        return (res//(pow(2, n)))%mod
        