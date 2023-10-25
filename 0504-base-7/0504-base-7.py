class Solution:
    def convertToBase7(self, num: int) -> str:
        ans = ''
        nums = abs(num)
        while nums:
            ans+= str(nums%7)
            nums//=7
        if num==0:
            ans +="0"
        return ans[::-1] if num>= 0 else "-"+ans[::-1]
        