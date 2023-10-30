class Solution:
    def hammingWeight(self, n: int) -> int:
        return int(str(n)).bit_count()