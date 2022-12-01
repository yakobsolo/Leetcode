class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l, sums,average,max_average = 0,0,float("-inf"),float("-inf")
        for r in range(len(nums)):
            sums += nums[r]

            if r >= k-1:
                average = sums/k
                sums-= nums[l]
                l+=1
            print(average)
            max_average = max(max_average, average)
        return max_average