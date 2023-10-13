class Solution:
    def countOrders(self, n: int) -> int:
        res = 1
        mod  = 10**9 + 7
        k = n*2
        # if n==1:
        #     return 1
        for _ in range(n*2):
            # print(k)
            res  =(res*k)
            k-=1
        return (res//(pow(2, n)))%mod
        