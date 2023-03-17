class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        
        def backtrack(index, path):
            if len(path) == k:
                
                ans.append(path[::])
                return
            if index == n+1:
                return 
            path.append(index)
            backtrack(index+1, path)
            path.pop()
            backtrack(index+1, path)
            
           
        backtrack(1, [])
        return ans