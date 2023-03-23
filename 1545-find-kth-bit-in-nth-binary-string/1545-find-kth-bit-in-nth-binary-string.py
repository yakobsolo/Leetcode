class Solution:
    
    def findKthBit(self, n: int, k: int) -> str:
        
        def reverse(s):
                return s[::-1]

        def invert(s):
            s = list(s)
            for i in range(len(s)):
                if s[i] == "1":
                    s[i] = "0"
                else:
                    s[i] = "1"
            return "".join(s)
            
        def find(n):
            
            if n == 1:
                return "0"
            temp = find(n-1)
            inver = invert(temp)
            rever = reverse(inver)
            one = "1"
            strg = temp + one + rever
            
            return strg
        ans = find(n)
        print(ans)
        return ans[k-1]
        