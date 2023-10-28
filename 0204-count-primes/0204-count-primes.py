class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n<2: return 0
        
        primes = [1]*n
        primes[0], primes[1] =0, 0
        for i in range(2, ceil(sqrt(n))):
            if primes[i] == 1:
                primes[i*i::i] = [0]*len(primes[i*i::i])
        
        return sum(primes)
                