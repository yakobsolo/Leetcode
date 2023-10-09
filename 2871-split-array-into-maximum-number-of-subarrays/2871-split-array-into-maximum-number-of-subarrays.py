class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        N = len(nums)
        
        mn = nums[0]
        for i in range(1, N):
            mn &= nums[i]
        count = 0
        if mn == 0:
            i = 0
            
            while i<N:
                cur = nums[i]
                # print(i, cur, "in")
                if cur == 0:
                    i +=1
                    count+=1
                    continue
                while i <N-1:
                    i+=1
                    
                    cur = cur & nums[i]
                    # print(i, cur)
                    if cur == 0:
                        count+=1
                        break
                i+=1
            return count
                
                
            
            
        else:
            return 1
            