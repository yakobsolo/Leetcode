class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_cap = ship_max = sum(weights)
        ship_min = max(weights)
        
        while ship_min<=ship_max:
            mid = (ship_min+ship_max)//2
            day = 1
            sums = 0
            for i in range(len(weights)):
                sums += weights[i]
                
                if sums> mid:
                    day+=1
                    sums = weights[i]
               
                    
              
            
            
            if day> days:
                
                ship_min = mid+ 1
            elif day<= days:
                ship_max = mid-1
                min_cap = min(min_cap, mid)
            
            
                
        return min_cap
            
            
                
                
        