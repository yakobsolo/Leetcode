class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l, n = 0, len(nums)
        hash = defaultdict(int)
        max_ans = 0
        sums = 0
        for r in range(n):
            hash[nums[r]] +=1
            sums += nums[r]
            if r-l+1==k:
                print(r, l)
                if len(hash) ==k:
                    max_ans = max(max_ans, sums)
                    sums -= nums[l]
                    hash[nums[l]] -=1
                    
                    if hash[nums[l]] == 0:
                        del hash[nums[l]]
                    l+=1
                else:
                    sums -= nums[l]
                    hash[nums[l]] -=1
                    if hash[nums[l]] == 0:
                        del hash[nums[l]]
                    l+=1       
      
        return max_ans
            