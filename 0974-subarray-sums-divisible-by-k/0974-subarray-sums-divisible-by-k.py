class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hashmap = {0: 1}
        prefix = []
        prefix.append(nums[0])
        res = 0
        
        for i in range(1, len(nums)):
            prefix.append(prefix[i-1] + nums[i])
        
        for i in range(len(prefix)):
            mod = prefix[i]%k
            if mod in hashmap:
                res+= hashmap[mod]
            hashmap[mod]= 1+ hashmap.get(mod, 0)
        return res
            