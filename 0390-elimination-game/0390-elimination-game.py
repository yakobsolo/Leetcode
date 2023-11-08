class Solution:
    def lastRemaining(self, n: int) -> int:
        left = True  
        remaining = n  
        step = 1  
        head = 1  
        
        while remaining > 1:
           
            if left or remaining % 2 == 1:
                head += step
                
            step *= 2  
            remaining //= 2  
            left = not left  

        return head
    
 

        
        
        
            
            
            
            
            
        