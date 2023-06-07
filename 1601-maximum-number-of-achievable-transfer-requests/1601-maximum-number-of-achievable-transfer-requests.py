class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        path = [0 for i in range(n)]
        ans = 0
        leng = len(requests)
        def backtrack(i, c):
            nonlocal ans
            if i == leng:
                if path.count(0) != n: return 
                ans = max(ans,c)
                return 
            path[requests[i][0]]-=1
            path[requests[i][1]] +=1
            backtrack(i+1,c+1)
            path[requests[i][0]]+=1
            path[requests[i][1]] -=1
            backtrack(i+1, c)
        backtrack(0, 0)
        return ans