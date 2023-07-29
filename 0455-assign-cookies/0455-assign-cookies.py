class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count = 0
        n, m = len(g), len(s)
        i , j = 0, 0
        while i<n and j<m:
            if s[j] >= g[i]:
                count +=1
                j+=1
                i+=1
            else:
                j+=1
        return count