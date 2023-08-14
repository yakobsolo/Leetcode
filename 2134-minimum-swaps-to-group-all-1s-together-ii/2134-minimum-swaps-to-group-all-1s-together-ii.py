class Solution:
    
    def minSwaps(self, nums: List[int]) -> int:
        b = len(nums)
        arr = nums
        arr += nums
        n = len(arr)
        # print(nums)
        n_one = 0
        for i in range(b):
            if nums[i] == 1:
                n_one +=1
        l = 0
        # print(n_one)
        count_one = 0
        min_count = n+1
        for r in range(n):
            if r -l +1 > n_one :
                count_one -= nums[l]
                l+=1
            # print(r, arr[r], count_one)
            if arr[r] == 1:
                count_one +=1

            if r - l+1 == n_one:
                min_count = min(min_count, n_one - count_one)

            # print(count_one, min_count, "count")
        return min_count