class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = [pref[0]]
        prev = 0
        for n in pref[1:]:
            
            arr.append(arr[-1]^n)
            if prev:
                arr[-1] = arr[-1]^prev
                cur = prev
                prev = cur ^ arr[-2]
            else:
                prev = arr[-2]
        return arr