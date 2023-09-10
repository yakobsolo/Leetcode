class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        
        price.sort()
        l, r= 0 , price[-1]- price[0]
        n = len(price)
        def checker(mid):
            last , pair = price[-1], 0
            for r in range(n):
                if abs(price[r] - last) >= mid:
                    pair +=1
                    last = price[r]
                if pair == k:
                    return True
            return False
        
        while l<r:
            mid = l + (r-l +1)//2
            
            if checker(mid):
                l = mid
            else:
                r = mid-1
                
        return l