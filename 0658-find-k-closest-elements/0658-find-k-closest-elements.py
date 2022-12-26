class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ans, res = [],[]
        for i in range(len(arr)):
            res.append([abs(arr[i] - x), arr[i]])
        
        res = sorted(res, key=lambda x: x[0])
        for i in range(k):
            ans.append(res[i][1])
        

        
        
        return sorted(ans)