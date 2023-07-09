class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = defaultdict(list)
        n = len(nums)
        max_idx = [1, 0]
        for i in range(n):
            dp[i].append(nums[i])
            if i >= 1:
                mx  = 1
                mx_idx = i
                for j in range(i-1, -1, -1):
                    if nums[i]%nums[j] == 0:
                        cur = len(dp[j])
                        if cur >= mx:
                            mx = cur
                            mx_idx = j
                if mx_idx != i and mx+1>max_idx[0]: max_idx = [mx, i]
                if mx >= 1 and mx_idx != i:
                    dp[i]+=(dp[mx_idx])
        
        return dp[max_idx[1]]
                