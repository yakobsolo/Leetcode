class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        right , n = 0 , len(nums)
        pairs =0
        # calcpairs = lambda x: (x*(x-1))//2
        GoodSubArray =0
        for l in range(n):
            while right<n and  pairs < k:
                count[nums[right]] +=1
                pairs += count[nums[right]]-1
                right +=1
            if pairs>=k:
                GoodSubArray += n-right+1
                pairs -= (count[nums[l]] -1)
                count[nums[l]] -=1
        return GoodSubArray
                
            
                
                
            
            
            
                
                