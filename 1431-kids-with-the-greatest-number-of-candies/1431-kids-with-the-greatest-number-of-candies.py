class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxx = max(candies)
        n = len(candies)
        res = [False]*n
        for i in range(n):
            if candies[i] + extraCandies >= maxx: res[i] = True
        return res