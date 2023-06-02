class Solution:
    def numDecodings(self, s: str) -> int:
        arr = set([str(i) for i in range(1 ,27)])
        # print(arr)
        # print(s[0:3])
        # return 1
        
        memo = defaultdict(int) 
        n = len(s)
        def dp(i, k):
            
            if i==n: 
                return k%2
            if i > n: return 0
            # if i==k  and s[i] not in arr: return 0
            # print(s[i:i+k] in arr,s[i:i+k])
            if s[i:i+k] and s[i:i+k] not in arr: return 0
            if (i, k) not in memo:
                memo[(i, k)] = dp(i+k,1) + dp(i+k,2)
             
            return memo[(i, k)]
        
        return dp(0, 0)