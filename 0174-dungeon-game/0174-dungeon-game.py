class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n, m = len(dungeon), len(dungeon[0])
        dp = [[0 for i in range(m+1)] for j in range(n+1)]
        
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                
                if dp[i+1][j] == 0 and dp[i][j+1] == 0: 
                    # print(i, j, "in")
                    if dungeon[i][j] >=0: dp[i][j] = 1
                    else:
                        dp[i][j] = abs(dungeon[i][j]) +1
                
                else:
                    
                    if dp[i+1][j] == 0 and dp[i][j+1] != 0:
                        
                        temp = dp[i][j+1]
                        temp -= dungeon[i][j]
                        if temp<=0:
                            dp[i][j] = 1
                        else:
                            dp[i][j] = temp
                    elif dp[i+1][j] != 0 and dp[i][j+1] == 0:
                         
                        temp = dp[i+1][j]
                        temp -= dungeon[i][j]
                        if temp<=0:
                            dp[i][j] = 1
                        else:
                            dp[i][j] = temp
                    else:
                        temp = min(dp[i+1][j] , dp[i][j+1])
                        
                        temp -= dungeon[i][j]
                        if temp<=0:
                            dp[i][j] = 1
                        else:
                            dp[i][j] = temp
        return dp[0][0]
                        
        
        