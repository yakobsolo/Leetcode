class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        mx = 0
        for i in range(len(nums)):
            
            if nums[i]%2== 0 and nums[i]<= threshold:
                cur = i
                mx = max(mx, 1)
                for j in range(i+1, len(nums)):
                    if nums[cur] %2 != nums[j]%2 and nums[j]<= threshold:
                        cur  = j
                        mx = max(mx, j-i+1)
                        # print(nums[j], i)
                    else:
                        break
        return mx
                        
                    