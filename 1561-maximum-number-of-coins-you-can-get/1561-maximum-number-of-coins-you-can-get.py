class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        sum = 0
        j = len(piles) - 2
        piles.sort()
        for i in range(int(len(piles) / 3)):
            medium = piles[j]
            sum = sum + medium
            j = j - 2
        return sum