class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        P = [1] * n
        for i in range(n):
            print((i - nums[i] + 1) % n)
            P[(i - nums[i] + 1) % n] -= 1
        print(P)
        P = list(accumulate(P))
        return P.index(max(P))