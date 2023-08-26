class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        hash = [-1, -1, -1]
        ans = 0
        for i, c in enumerate(s):
            hash[ord(c) - 97] = i
            ans += min(hash) +1
            
             
               
        return ans
                
         
        
