class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        hash = defaultdict(int)
        prefixsum = 0
        m = len(nums)
        prefix = [0]*(m+1)
        max_unq = 0
        l = -1
        for i, n in enumerate(nums):
            prefixsum += n
            prefix[i] = prefixsum
            if n not in hash:
                max_unq = max(max_unq, prefix[i]-prefix[l])
            else:
                if hash[n]>l:
                    l = hash[n]
                    max_unq = max(max_unq, prefix[i] - prefix[l])
                else: max_unq = max(max_unq, prefix[i]-prefix[l])
            hash[n] = i
            
            
        return max_unq
                
            