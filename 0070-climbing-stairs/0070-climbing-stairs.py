class Solution:
   
    def climbStairs(self, n: int) -> int:
        
        memo = {}
        def dp(i):
            if i == n:
                return 1
            if i >n:
                return 0
            if i not in memo:
                left = dp(i+1)
                right = dp(i+2)
                memo[i] = left + right
                
            
            return memo[i]
        return dp(0)
        
#         if n< 3:
#             return n
        
#         if n not in self.memo:
#             self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
#         return self.memo[n]