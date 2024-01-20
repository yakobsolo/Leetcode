class Solution:
    def minPartitions(self, n: str) -> int:
        
        mx = 9
        while True:
            if str(mx) in n:
                return mx
            mx-=1
        