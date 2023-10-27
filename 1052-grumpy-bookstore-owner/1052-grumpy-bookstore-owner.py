class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        N = len(customers)
        tot = 0
        grmpy = 0
        l, r = 0, 0
        temp = 0
        while r<N:
            
            while r<N and r-l+1<=minutes:
                if grumpy[r] == 1:
                    temp+=customers[r]
                    
                else:
                    tot+=customers[r]
                r+=1
            grmpy = max(grmpy, temp)
            if grumpy[l]==1:
                temp-=customers[l]
            l+=1
            # print(r)
        return tot+grmpy
                    
                    