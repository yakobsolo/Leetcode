class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        nums = list(map(int, ''.join(map(str, nums))))
        return nums