class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones = Counter(stones)
        count = 0
        for jewel in jewels:
            count += stones[jewel]
        return count