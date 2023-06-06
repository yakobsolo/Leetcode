class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        n = len(coins)
        def dp(i, a):
            if a == amount: return 1
            if a>amount: return 0
            if i== n: return 0
            
            if (i, a) not in memo:
                memo[(i, a)] = dp(i, a+coins[i]) + dp(i+1, a)
            return memo[(i, a)]
        return dp(0, 0)