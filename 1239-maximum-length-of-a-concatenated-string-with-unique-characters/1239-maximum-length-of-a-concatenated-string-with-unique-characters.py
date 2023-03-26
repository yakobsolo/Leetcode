class Solution:
    def maxLength(self, arr: List[str]) -> int:
        ans = 0 
        def unique(path, concate):
            
            
            
            count = "".join(path)
            if len(set(count)) != len(count) or len(set(concate)) != len(concate):
                return False
            for c in concate:
                if c in count:
                    return False
            return True
        
        def maxconcat(idx, path):
            nonlocal ans
            if idx == len(arr):
                

                strg = "".join(path)
                if len(set(strg)) != len(strg):
                    return 
                ans = max(ans, len(strg))
                return 
            
            if not path or unique(path, arr[idx]):
                
                maxconcat(idx+1, path + [arr[idx]])
            
            maxconcat(idx+1, path)
        maxconcat(0, [])
        return ans
                