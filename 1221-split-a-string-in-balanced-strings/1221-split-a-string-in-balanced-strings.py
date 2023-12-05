class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l_c = r_c = 0
        ans  = 0
        
        for n in s:
            if n == "L": l_c+=1
            if n == "R": r_c +=1
            
            if l_c == r_c:
                l_c=r_c = 0
                ans+=1
            
        
        return ans
            