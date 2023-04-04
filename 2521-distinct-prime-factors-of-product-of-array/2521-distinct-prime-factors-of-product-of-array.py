class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        x = 1
        factorization = set()
        def prime(x):
            d = 2
            while d**2 <= x:
                while x%d == 0:
                    factorization.add(d)
                    x//=d
                d+=1
            if x>1:
                factorization.add(x)
            return factorization 
        
        ans = set()
        for n in nums:
            
            if n.bit_count() == 1:
                ans.add(2)
            else:
                ans.update(prime(n))            
        
        
            
        return len(ans)    