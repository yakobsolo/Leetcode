class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minban , maxban = 1, max(piles)
        mink = maxban
        def helper(ban):
            hour = 0
            curban = ban
            
            for pile in piles:
                hour += (pile//ban)
                if pile % ban:
                    hour+=1
            if hour <= h:
                return True
            else: False
                
        
        while minban<=maxban:
            k = minban + (maxban-minban)//2
            # print(k)
            
            if helper(k):
                mink = min(mink, k)
                # print(mink, k)
                maxban = k-1
            else:
                minban = k+1
        
        return mink