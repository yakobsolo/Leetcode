class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        n = len(s)
        if n<4 and n>12: return ans
        
        def backtrack(i, fs, path):
            
            if i == n and fs==4:
                ans.append(path[:-1])
                return 
            if i>=n: return 
            if fs>4: return 
            
            for j in range(i, (i+3)):
                # print(i, j)
                if int(s[i:j+1]) < 256 and (i == j or s[i]!="0"):
                    backtrack(j+1, fs+1, path+s[i:j+1] + ".")
        backtrack(0, 0, "")
        return ans