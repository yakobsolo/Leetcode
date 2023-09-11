class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        
        nums.sort()
        n = len(nums)
        def checker(mid):
            req_op = 0
            for i in range(n-1, -1, -1):
                if nums[i] >mid:
                    req_op += (nums[i]-1)//mid
                    if req_op>maxOperations: return False
                elif nums[i]<mid: return True
            return True
                    
        
        
        l, r = 1, nums[-1]
        while l<r:
            mid = l+ (r-l)//2
            
            if checker(mid):
                r = mid
            else:
                l = mid +1
        return r