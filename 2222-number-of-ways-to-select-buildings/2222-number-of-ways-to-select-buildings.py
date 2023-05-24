class Solution:
    def numberOfWays(self, s: str) -> int:
        preones = s.count("1")
        prezeros = s.count("0")
        
        ones, zeros = 0, 0
        ans = 0
        for c in s:
            if c == "0":
                ans += ones * (preones-ones)
                zeros +=1
            if c == "1":
                ans += zeros * (prezeros -zeros)
                ones +=1
            
        return ans