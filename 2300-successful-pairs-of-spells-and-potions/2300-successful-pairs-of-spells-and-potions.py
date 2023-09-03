class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(spells)
        m = len(potions)
        ans = []
        for s in spells:
            find = ceil(success/s)
            l = bisect_left(potions, find)
            print(find, l)
            ans.append(m-l)
        return ans