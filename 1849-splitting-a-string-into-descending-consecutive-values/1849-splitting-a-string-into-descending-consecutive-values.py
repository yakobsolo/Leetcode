class Solution:
    def splitString(self, s: str) -> bool:
        ans = []
        def splitS(index):
            if index == len(s):
                return len(ans) >= 2
            
            
            for j in range(index, len(s)):
                cur = int(s[index: j+1])
                if ans == [] or ans[-1]-1  == cur:
                    ans.append(cur)
                    if splitS(j+1):
                        return True
                    ans.pop()
            return False
        
      
        return splitS(0)