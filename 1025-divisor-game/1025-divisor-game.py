class Solution:
    def divisorGame(self, n: int) -> bool:
        dp = False
        i = 0
        for i in range(2, n+1):
            dp = not dp
        return dp