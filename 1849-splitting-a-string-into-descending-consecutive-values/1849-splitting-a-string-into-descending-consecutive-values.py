class Solution:
    def splitString(self, s: str) -> bool:
        
        def splitS(index, prev):
            if index == len(s):
                return True
            
            for j in range(index, len(s)):
                cur = int(s[index: j+1])
                if cur+1 == prev and splitS(j+1, cur):
                    return True
            return False
        
        for i in range(len(s) -1):
            val = int(s[:i+1])
            if splitS(i+1, val): return True
        return False