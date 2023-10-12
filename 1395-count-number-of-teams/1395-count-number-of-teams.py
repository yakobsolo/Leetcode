class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        prevsmaller = []
        prevgreater = []
        nextsmaller = []
        nextgreater = []
        N = len(rating)
        for i in range(N):
            nxg, nxs = 0, 0
            for j in range(i, N):
                if rating[j] >rating[i]:
                    nxg +=1
                if rating[j] < rating[i]:
                    nxs +=1
            nextsmaller.append(nxs)
            nextgreater.append(nxg)
        for i in range(N-1, -1, -1):
            prs, prg = 0, 0
            for j in range(i-1, -1, -1):
                if rating[j]<rating[i]:
                    prs+=1
                if rating[j]>rating[i]:
                    prg+=1
            prevsmaller.append(prs)
            prevgreater.append(prg)
        prevsmaller = prevsmaller[::-1]
        prevgreater = prevgreater[::-1]
        
        res = 0
        # print(nextgreater, prevsmaller)
        for i in range(N):
            res=res + prevsmaller[i]*nextgreater[i] + prevgreater[i]*nextsmaller[i]
        return res
                
            
            
            
            