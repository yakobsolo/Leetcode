class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = [pref[0]]
        temp = []
        for n in pref[1:]:
            
            arr.append(arr[-1]^n)
            if temp:
                arr[-1] = arr[-1]^temp[-1]
                temp.append(arr[-2]^temp[-1])
            else:
                temp.append(arr[-2])
        return arr