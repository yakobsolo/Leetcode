class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = [0,*list(accumulate(nums))]
        
        
    def sumRange(self, left: int, right: int) -> int:
        ans = self.prefix[right+1] - self.prefix[left]
        return ans
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)