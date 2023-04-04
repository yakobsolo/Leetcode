class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        leng = len(nums)
        hash = {}
        for i in range(leng):
            if nums[i] not in hash:
                hash[nums[i]] = 1
            else:
                hash[nums[i]] +=1
        sortedhash = sorted(hash.items(), key=lambda x:x[-1])
        return sortedhash[0][0]