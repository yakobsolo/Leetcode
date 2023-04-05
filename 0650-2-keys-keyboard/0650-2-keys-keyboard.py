class Solution:
    def minSteps(self, n: int) -> int:
        
        if n == 1:
            return 0
        primefactorizations = []
        def factorization(n):
            d = 2
            while d ** 2<= n:
                
                while n%d == 0:
                    primefactorizations.append(d)
                    n//=d
                d +=1
            if n> 1:
                primefactorizations.append(n)
        factorization(n)
        return sum(primefactorizations)
        