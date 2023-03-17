class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def validPalindrome(s: str) -> bool:
            l,r = 0, len(s) -1
            while l<r:

                if s[l] != s[r]:
                    return False

                l += 1
                r -= 1
            return True
        
        
        
        
        ans = []
        path = []
        
        def back(index, path):
            if index == len(s):
                ans.append(path[:])
                return
            
            for j in range(index, len(s)):
                cur = s[index: j+1]
                
                if validPalindrome(cur):
                    path.append(cur)
                    back(j+1, path)
                    path.pop()
            return 
            
        for i in range(len(s)):
            val = s[: i+1]
            if validPalindrome(val):
                path.append(val)
                back(i+1, path)
                path.pop()
        return ans