class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [0]*len(s)
        
        for i, n in enumerate(indices):
            ans[n] = s[i]
            
        return "".join(ans)