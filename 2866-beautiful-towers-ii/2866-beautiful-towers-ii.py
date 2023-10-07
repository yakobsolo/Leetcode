class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
      
        n = len(maxHeights)
        
        s = []
        prv = [0] * n
        nxt = [0] * n
        lft = [0] * n
        rgt = [0] * n
        
        for j in range(n):
            while s and maxHeights[s[-1]] >= maxHeights[j]:
                s.pop()
            
            prv[j] = -1 if not s else s[-1]
            s.append(j)
        
        s.clear()
        
        for j in range(n - 1, -1, -1):
            while s and maxHeights[s[-1]] >= maxHeights[j]:
                s.pop()
            
            nxt[j] = n if not s else s[-1]
            s.append(j)
        
        for j in range(n):
            lft[j] = maxHeights[j]
            
            if j == 0:
                continue
            
            if maxHeights[j] >= maxHeights[j - 1]:
                lft[j] += lft[j - 1]
            else:
                lft[j] += (j - prv[j] - 1) * maxHeights[j] + (0 if prv[j] < 0 else lft[prv[j]])
        
        for j in range(n - 1, -1, -1):
            rgt[j] = maxHeights[j]
            
            if j == n - 1:
                continue
            
            if maxHeights[j] >= maxHeights[j + 1]:
                rgt[j] += rgt[j + 1]
            else:
                rgt[j] += (nxt[j] - j - 1) * maxHeights[j] + (0 if nxt[j] >= n else rgt[nxt[j]])
        
        ans = 0
        for j in range(n):
            ans = max(ans, lft[j] + rgt[j] - maxHeights[j])
        
        return ans
