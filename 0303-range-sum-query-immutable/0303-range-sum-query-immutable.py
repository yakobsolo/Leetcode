class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        
        
    def sumRange(self, left: int, right: int) -> int:
        
#         self.nums.append(0)
#         self.nums = [0]+self.nums[]
        leftsum = 0
        rightsum =0
        
        total = sum(self.nums)
        for i in range(right+1,len(self.nums)):
            rightsum += self.nums[i]
        for j in range(left):
            leftsum += self.nums[j]
        
            
        
        ans = total- leftsum - rightsum
        return ans
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)