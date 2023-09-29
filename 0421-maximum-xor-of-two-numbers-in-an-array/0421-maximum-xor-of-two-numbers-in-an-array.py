
        
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_len = len(bin(max(nums))) - 2             
        
        root = {}
        
        
        for num in nums:
            node = root 
            for shift in range(max_len, -1, -1):           
                val = 1 if num & (1 << shift) else 0      
                if val not in node:
                    node[val] = {}
                node = node[val]
                
        ans = 0
        for num in nums:                              
            node = root
            mx = 0
            for shift in range(max_len, -1, -1):
                val = 1 if num & (1 << shift) else 0  
                if 1-val in node:
                    node = node[1-val]
                    mx +=2**shift
                else:
                    node = node[val]
            ans = max(ans, mx)            
        return ans  