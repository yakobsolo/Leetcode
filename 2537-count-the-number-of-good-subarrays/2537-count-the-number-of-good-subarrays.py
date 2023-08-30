class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        l , n = 0 , len(nums)
        total =0
        calcpairs = lambda x: (x*(x-1))//2
        GoodSubArray =0
        for right in range(n):
            count[nums[right]] +=1
            diff = calcpairs(count[nums[right]]) - calcpairs(count[nums[right]] -1)
            
            total += diff
            while total>=k:
                GoodSubArray += n-right
                diff = calcpairs(count[nums[l]]) - calcpairs(count[nums[l]] -1)
                total -= diff
                
                count[nums[l]]-=1
                l +=1
        return GoodSubArray
                
                