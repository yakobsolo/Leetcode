class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        max_diff = 0
        N = len(nums)
        for i in range(N):
            max_diff = max(max_diff, nums[i] - nums[i-1])
        
        l = 0
        r = max_diff
        
        def checker(m, p):
            
            l,r = 0, 1
            while r <  N and p>0:
                if nums[r] - nums[l] <= mid:
                    l +=2
                    r +=2
                    p-=1
                else:
                    l+=1
                    r+=1
            if p== 0: return True
            else: return False
                
                
        # print(max_diff)
        while l<r:
            mid = l+(r-l)//2
            if checker(mid, p):
                # print(mid, "true")
                r = mid 
            else:
                # print(mid, "false")
                l= mid +1
        return r
        
        # 1 1 2 3 7 10