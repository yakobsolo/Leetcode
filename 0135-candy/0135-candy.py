class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left_nei = [1]*n
        right_nei = [1]*n
        
        
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                left_nei[i] =left_nei[i-1] + 1
        for i in range(n-2, -1,-1):
            if ratings[i] > ratings[i+1]:
                right_nei[i] =right_nei[i+1]+1
        tot = 0      
        for i in range(n):
            tot += max(left_nei[i], right_nei[i])
        return tot