class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        
        
        mn = inf
        n = len(beans)
        sm = sum(beans)
        prefix = [0]*(n+1)
        for i in range(n):
            prefix[i]+=prefix[i-1]+beans[i]
        # print(beans)
        # print(prefix)
        for i in range(n-2, -1, -1):
            # print(i, sm-prefix[i-1] - (n-1-i)*beans[i] )
            mn = min(mn, sm-prefix[i] - (n - 1 - i ) * beans[i] + prefix[i-1], prefix[i]+sm-prefix[i+1] - (n-2-i)*beans[i+1]  )
        if mn == inf: return 0
        return mn
        
        