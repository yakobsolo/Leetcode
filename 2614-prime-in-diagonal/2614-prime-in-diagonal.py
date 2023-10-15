class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        N = len(nums)
        def isPrime(n):
            d = 2
            if n ==1:
                return False
            while d*d <= n:
                if n%d == 0:
                    return False
                d+=1
            return True
        
        mx = 0
        for i in range(N):
            
            if isPrime(nums[i][i]):
                mx = max(mx, nums[i][i])
            if isPrime(nums[i][N-i-1]):
                mx = max(mx, nums[i][N-i-1])
        return mx