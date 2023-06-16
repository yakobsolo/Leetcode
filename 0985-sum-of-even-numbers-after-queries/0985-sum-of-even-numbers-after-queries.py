class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sums = 0
        for n in nums:
            if not n%2: sums += n
        res = [0]*len(queries)
        i = 0
        for q in queries:
            v, idx = q
            if not nums[idx]%2:
                sums -= nums[idx]
            nums[idx] += v
            if not nums[idx]%2:
                sums+=nums[idx]
                res[i] = sums
            else:
                res[i] = sums
            i+=1
        return res
                