class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        arr = []
        for i in range(n):
            arr.append(nums[i])
            for j in range(i+1, n):
                arr.append(arr[-1]+nums[j])
        arr.sort()
        ans= 0
        print(arr)
        while left<=right:
            ans+=arr[left-1]
            left+=1
        return ans % (10**9 + 7)
            
                
                