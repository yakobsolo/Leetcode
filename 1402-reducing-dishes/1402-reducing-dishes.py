class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        max_sum = 0
        n = len(satisfaction)
        satisfaction.sort()
        for i in range(n):
            j = 1
            sums = 0
            for k in range(i, n):
                sums+=satisfaction[k]*j
                j+=1
            max_sum = max(max_sum, sums)
        if max_sum<0:
            return 0
        return max_sum