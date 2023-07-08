class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0: return True
        prev = 0
        k , i= len(flowerbed), 0
        while n>0 and i<k:
            if flowerbed[i] != 1:
                if prev != 1:
                    if i+1<k and flowerbed[i+1] == 1:
                        i+=1
                        continue
                    n-=1
                    prev = 1
                    if n == 0: return True
                else:
                    prev = 0
            else:
                prev = 1
            i+=1
        return False
                