class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        
        if h >= sum(piles):
            return 1
        min_k = k_max = max(piles)
        k_low = 1
        
        
        while k_low <= k_max:
            hour = 0

            mid = (k_low + k_max) // 2
            for i in range(len(piles)):
                if piles[i] > mid:
                    temp = piles[i]//mid
                    mod = piles[i]%mid
                    hour += temp
                    if mod != 0:
                        hour+=1
                else:
                    hour +=1 
            
            if hour > h:
                k_low = mid+1
            if hour <= h:
                min_k = min(min_k, mid)
                k_max = mid-1
        return min_k