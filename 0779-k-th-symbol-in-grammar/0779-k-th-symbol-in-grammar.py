class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        if n == 1:
            return 0
        
        parent = self.kthGrammar(n-1, ceil(k/2))
        iskodd = (k%2) == 1
        print(parent)
        if parent:
            return 1 if iskodd else 0
        else:
            return 0 if iskodd else 1
        