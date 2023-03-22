class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        times = 0
        i = 0
        leng = len(tickets)
        while tickets[k] != 0:
            if tickets[i] != 0:
                tickets[i] -=1
                
                times+=1
            
            i = (i+1) % leng
        return times