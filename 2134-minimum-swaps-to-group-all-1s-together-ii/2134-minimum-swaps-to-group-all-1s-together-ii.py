class Solution:
    
    def minSwaps(self, nums: List[int]) -> int:
        arr = nums
        arr += nums
        n = len(arr)
        n_one = nums.count(1)//2
        l = 0
        ones = []
        count_one = 0
        min_count = n+1
        print(nums, n_one)
        for r in range(n):
            if r -l +1 > n_one :
                count_one -= nums[l]
                l+=1

            if nums[r] == 1:
                count_one +=1

            if r - l+1 == n_one:
                min_count = min(min_count, n_one - count_one)


        return min_count