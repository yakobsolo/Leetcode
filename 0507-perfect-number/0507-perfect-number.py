class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        primes = {2, 3, 5, 7, 11, 13, 17, 19,23, 29, 31}
        def isPrime(x):
            d = 2
            while d*d <=x:
                if x%d == 0:
                    return False
                d+=1
            return True
        for item in primes:
            if isPrime(2**item -1):
                if (2**(item-1))*((2**item)-1) == num:
                    return True
        return False