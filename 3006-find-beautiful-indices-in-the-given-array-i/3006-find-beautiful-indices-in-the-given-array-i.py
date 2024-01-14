class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        aa = []
        bb = []
        
        N = len(s)
        
        ap = 0
        an = len(a)
        for i in range(N):
            if a[ap] == s[i]:
                ap +=1
                if ap == an:
                    aa.append(i-an+1)
                    ap = 0
            else:
                if s[i] == a[0]:
                    ap = 1
                else: ap = 0
        bp = 0
        bn = len(b)
        for i in range(N):
            if b[bp] == s[i]:
                bp +=1
                if bp == bn:
                    bb.append(i-bn+1)
                    bp = 0
            else: 
                if s[i] == b[0]:
                    bp  = 1
                else:
                    bp  = 0
        ans = []
        # print(aa, bb)
        for i in aa:
            for j in bb:
                if abs(j-i) <= k:
                    ans.append(i)
                    break
        return ans
                    
                    
                
            