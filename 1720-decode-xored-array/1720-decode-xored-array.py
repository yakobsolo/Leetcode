class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        encoded.insert(0, first)
        n = len(encoded)
        for i in range(1,n):
            encoded[i] = encoded[i-1]^encoded[i]
        return encoded