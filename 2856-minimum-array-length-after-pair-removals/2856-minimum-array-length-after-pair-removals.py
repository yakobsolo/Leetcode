from sortedcontainers import SortedList

class Solution:
    
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        count = Counter(nums)
        
        distinct = []
        for n in count.values():
            heappush(distinct, -n)
       
        while len(distinct) >= 2:
            a, b= heappop(distinct), heappop(distinct)
            # print(a, b)
            a+=1
            b+=1
            if a<0: heappush(distinct, a)
            if b<0: heappush(distinct, b)
        if not distinct: return 0
        return -heappop(distinct)
        
            