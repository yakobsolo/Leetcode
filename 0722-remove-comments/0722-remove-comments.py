class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res  = []
        new_s, blockend = "", False
        
        for s in source:
            i, n = 0, len(s)
            if not blockend: new_s = ""
            while i<n:
                 
                if blockend:
                    if s[i: i+2] == "*/" and i+1 < n:
                        blockend = False
                        i += 2
                    else:
                        i +=1
                else:
                    if s[i: i+2] == "/*" and i + 1< n:
                        i += 2
                        blockend = True
                        continue
                    if s[i: i+2] == "//" and i + 1< n:
                        break
                    
                    new_s += s[i]
                    i+=1
            if new_s and not blockend: res.append(new_s)
        return res