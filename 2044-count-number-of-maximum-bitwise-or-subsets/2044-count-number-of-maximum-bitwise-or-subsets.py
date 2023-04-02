class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        def maxBitOr(path):
            ans = 0
            for i in range(len(path)):
                if ans:
                    
                    ans = ans|path[i]
                else:
                    ans = path[i]
            return ans
        maxx = maxBitOr(nums)
        
        self.count = 0
        ans = []
        def subset(idx , path):
            if idx == len(nums):
                ans.append(path[:])
                if maxBitOr(path) == maxx:
                    self.count +=1
                return
            
            subset(idx+1, path + [nums[idx]])
            subset(idx+1, path)
            
            return
        subset(0, [])
        return self.count
            