class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        diff = set()
        houses.sort()
        heaters.sort()
        for h in houses:
            l = bisect_left(heaters, h)
            
            if l == 0:
                diff.add(heaters[0]-h)
            elif l==len(heaters):
                diff.add(h - heaters[-1])
            else:
                diff.add(min(heaters[l] - h, h - heaters[l-1]))
        return max(diff)