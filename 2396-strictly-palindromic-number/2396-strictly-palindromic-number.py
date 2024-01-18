class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        
        def ispalindrom(arr):
            l, r = 0, len(arr)-1
            while l<r:
                if arr[l] != arr[r]:
                    return False
                l+=1
                r-=1
            return True
        
        for i in range(2, n-1):
            b = []
            cur = n
            while  cur>=i:
                rm = cur%i
                b.append(rm)
                cur //= i
            b.append(cur)
                
            # print(b)
            if not ispalindrom(b):
                return False
        return True
            
            