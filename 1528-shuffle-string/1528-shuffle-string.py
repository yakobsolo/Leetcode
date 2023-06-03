class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [0]*len(s)
        i = 0
        for n in indices:
            ans[n] = s[i]
            i+=1
        return "".join(ans)