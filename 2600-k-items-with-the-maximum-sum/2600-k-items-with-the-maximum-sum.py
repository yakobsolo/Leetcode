class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ans = 0
        if k<=numOnes:
            return k
        
        ans +=numOnes
        k -=numOnes
        if k<=numZeros: return ans
        k -= numZeros
        return ans - k


