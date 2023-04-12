class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n = len(image)
        c = len(image[0])
        
        if image[sr][sc] == color:
            return image
                
            
        dl = [-1, 0, 1,0]
        dr = [0, 1, 0,-1]
        
        def flood(sr, sc, source):
            
            if sr< 0 or sc<0 or sr>= n or sc>=c:
                return 
            if image[sr][sc] != source:
                return 
            
            for i in range(4):    
                image[sr][sc] = color
                flood(sr+dl[i], sc + dr[i], source)
                    
                
        source = image[sr][sc]          
        flood(sr, sc, source)
        return image