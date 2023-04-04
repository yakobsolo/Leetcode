class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        hash = {}
        for n in deck:
            if n not in hash:
                hash[n] = 1
            else:
                hash[n] +=1

        prev = 0
        for key in hash:
            temp = hash[key]
            if gcd(prev, temp) == 1:
                return False
            prev = gcd(prev, temp)
        return True