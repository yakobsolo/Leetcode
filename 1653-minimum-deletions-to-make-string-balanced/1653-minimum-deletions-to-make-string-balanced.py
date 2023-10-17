class Solution:
    def minimumDeletions(self, s: str) -> int:
        N = len(s)
        res, bc = 0, 0
        for c in s:
            if c == "b":
                bc+=1
            elif bc:
                res+=1
                bc-=1
        return res