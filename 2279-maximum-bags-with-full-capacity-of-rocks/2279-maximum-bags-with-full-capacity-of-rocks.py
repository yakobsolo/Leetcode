class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        rem = [capacity[i] - rocks[i] for i in range(n)]
        rem.sort()
        count = 0
        
        for i in range(n):
            if additionalRocks >= rem[i]:
                count +=1
                additionalRocks-=rem[i]
            else: return count
        return count
        