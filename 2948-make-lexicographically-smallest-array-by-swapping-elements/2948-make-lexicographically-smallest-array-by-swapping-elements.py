class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        size = len(nums)
        pair = [[nums[i], i] for i in range(0, size)]
        pair.sort()

        result = [0] * size

        start = 0
        for end in range(0, size):
            if (end + 1 >= size or pair[end + 1][0] - pair[end][0] > limit):
                temp = [pair[i][1] for i in range(start, end + 1)]
                temp = sorted(temp)
                j = start
                for idx in temp:
                    result[idx] = pair[j][0]
                    j += 1
                start = end + 1

        return result