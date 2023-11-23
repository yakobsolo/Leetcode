class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = []
        for v in arr:
            if prefix:
                prefix.append(prefix[-1]^v)
            else:
                prefix.append(v)
                
        
        ans = []
        print(prefix)
        for l, r in queries:
            if l!=0:
                ans.append(prefix[r]^prefix[l-1])
            else:
                ans.append(prefix[r])
        return ans