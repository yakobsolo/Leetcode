class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for c in s:
            if c == "c":
                if stack:
                    bb = stack.pop()
                    if bb != "b": return False
                else:
                    return False
                
                if stack:
                    aa = stack.pop()
                    if aa != "a": return False
                else:
                    return False
            else:
                stack.append(c)
        if stack: return False
        return True
    
                
                