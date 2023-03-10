class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans = inf
        cookies.sort(reverse= True)
        def distribute(idx, path):
            nonlocal ans
            
            if ans <= max(path):
                return
            
            if idx == len(cookies):
                ans= min(ans,max(path))
                return 
            
            
            for child in range(k):
                path[child] += cookies[idx]
                distribute(idx+1, path)
                path[child] -= cookies[idx]
        distribute(0, [0]*k)
        return ans