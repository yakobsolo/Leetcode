class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod  = 10**9 + 7
        if n&1 == 1:
            n-=1
            n//=2
            ans = pow(20, n, mod)
            ans*=5
        else:
            ans  = pow(20, n//2, mod)
        return ans%mod