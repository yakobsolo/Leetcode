class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        leng = len(nums)
        count = 0
        
        def gcdd(a, b):
            if b == 0: return a
            return gcdd(b, a%b)
        
        for i in range(leng):
            prev = 0
            for j in range(i, leng):
                cur = gcdd(nums[j], prev)
                if cur == k:
                    count+=1
                prev = cur
                

        return count