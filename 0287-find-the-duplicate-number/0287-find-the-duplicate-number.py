class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap = Counter(nums)
        sortt = dict(sorted(hashmap.items(), key=lambda x:x[1]))
        sortlis = list(sortt)
        return sortlis[-1]