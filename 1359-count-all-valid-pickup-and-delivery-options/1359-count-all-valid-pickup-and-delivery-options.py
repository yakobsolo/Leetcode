class Solution:
    def countOrders(self, n: int) -> int:
        
        mod  = 10**9 + 7
        return (factorial(n*2)//(pow(2, n)))%mod
        