class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        N = len(ages)
        dp = [0]*N
        
        agess = []
        for i in range(N):
            agess.append((ages[i], scores[i]))
        
        agess.sort()
        # print(agess)
        dp[0] = agess[0][1]
        
        
        
        for i in range(N):
            for j in range(i-1,-1, -1):
                
                if agess[i][1] >= agess[j][1]  or agess[i][0] == agess[j][0]:
                    # print(i, j)
                    dp[i] = max(dp[i], dp[j] + agess[i][1])
                    # print(dp[i] , agess[i][1], dp[j])
                else:
                    dp[i] = max(dp[i], agess[i][1])
        # print(dp)
        return max(dp)