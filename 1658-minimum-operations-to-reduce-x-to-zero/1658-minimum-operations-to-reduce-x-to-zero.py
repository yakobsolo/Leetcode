class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        prefixSum =0
        back = {}
        
        prefixSum = 0
        back[0] = 0
        for i in range(n-1, -1, -1):
            prefixSum += nums[i]
            back[prefixSum] = n-i
        

        prefix = 0
        op = 0
        if prefixSum == x: return n
       
        res = inf
        if x in back:
            res = back[x]
        for i in range(n):
            prefix += nums[i]
            temp= x-prefix
            if temp<0: break
            op+=1
            
            if temp in back and back[temp]+op < n:
                res = min(res, op+back[temp])
                
       
        return res if res != inf  else -1
        
            
        
            
            