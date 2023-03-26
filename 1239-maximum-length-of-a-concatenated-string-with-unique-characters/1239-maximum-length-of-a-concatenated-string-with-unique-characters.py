class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.ans = 0 

        def maxconcat(idx, path):
            
            strg = "".join(path)
            if len(set(strg)) < len(strg):
                return 
                
            self.ans = max(self.ans, len(strg))
            for i in range(idx, len(arr)):
                maxconcat(i+1, path + [arr[i]])
            
            
        maxconcat(0, [])
        return self.ans
                