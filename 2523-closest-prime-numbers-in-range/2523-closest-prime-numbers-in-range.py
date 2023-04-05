class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        if left ==1 and right == 1:
            return [-1, -1]
        is_prime= [True for _ in range(right + 1)]
        is_prime[0] = is_prime[1] = False

        i = 2
        while i <= right:
            if is_prime[i]:
                j = 2 * i
                while j <= right:
                    is_prime[j] = False
                    j += i
            i += 1
        
        primes = []
        for i in range(left, right+1):
            if is_prime[i]:
                primes.append(i)
                
        leng= len(primes)
        mn = right+1
        for r in range(1, leng):
            if primes[r] - primes[r-1] < mn:
                mn=primes[r] - primes[r-1]
                temp = [primes[r-1], primes[r]]
            
        if leng == 1 or not primes:
            return [-1, -1]
        else:
            return temp