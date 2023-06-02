class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured< 1: return 0
        dp = [[0] *i for i in range(1, 101)]
        dp[0][0] = poured
        
        for i in range(99):
            flag = 0
            if i == query_row+1: 
                return dp[query_row][query_glass] if dp[query_row][query_glass] <1 else 1
            for j in range(i+1):
                if dp[i][j] - 1 <= 0:
                     continue   
                flag += 1
                dp[i+1][j] += (dp[i][j]-1)/2
                dp[i+1][j+1] += (dp[i][j]-1)/2
                dp[i][j] = 1
                
            if flag == 0:
                return dp[query_row][query_glass] if dp[query_row][query_glass] <1 else 1
        return dp[query_row][query_glass] if dp[query_row][query_glass] <1 else 1
                
                
                