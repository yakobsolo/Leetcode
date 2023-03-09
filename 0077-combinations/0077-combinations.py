class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        lis = []
        
        def backtrack(index, n):
            if len(lis) == k:
                
                ans.append(lis[::])
                return
          
            for i in range(index, n):
                lis.append(i)
                backtrack(i+1, n)
                lis.pop()
        backtrack(1, n+1)
        return ans