class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        binary = [0] * 32
        leng = len(nums)
        negativecount = 0
        for i in range(leng):
            if nums[i] < 0: 
                negativecount +=1
            num = abs(nums[i])
            for j in range(num.bit_length()):
                if num & (1<<j):
                    binary[j] +=1
        ans = 0
        for i in range(32):
            if binary[i] % 3 != 0:
                ans += 2**i
        if negativecount%3 != 0:
            return -ans
        else:
            return ans