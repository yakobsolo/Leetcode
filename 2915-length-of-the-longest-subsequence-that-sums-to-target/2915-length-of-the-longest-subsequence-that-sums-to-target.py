class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        N  = len(nums)

        dp = [[-1]*(target+1) for _ in range(N+1)]
        def find(idx, tgt):
        
            if tgt == 0:
                return 0
            if idx == N or tgt<0:
                return -inf
            if dp[idx][tgt]!=-1: return dp[idx][tgt]
            res = max(1 + find(idx + 1, tgt - nums[idx]), find(idx + 1, tgt))
            dp[idx][tgt] = res
            return res


        ans = find(0, target)
        if ans<0: return -1
        return ans