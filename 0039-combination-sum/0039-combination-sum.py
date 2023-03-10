class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        
        def combination(index, path):
            if index >= len(candidates):
                return
            if sum(path) == target:
                ans.append(path[:])
                return 
            if sum(path) >target:
                return
            path.append(candidates[index])
            combination(index, path)
            path.pop()
            combination(index+1, path)
        combination(0, [])
        
        return ans
        