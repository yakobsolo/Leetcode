class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascalTriangle = [1]
        if rowIndex == 0:
            return [1]
        
        def recursion(rowIndex):
            nonlocal pascalTriangle
            row = []
            if rowIndex == 0:
                return pascalTriangle
            
            temp = [0]+pascalTriangle+[0]
            r = 0
            leng = len(temp) -1
            def recurtiontemp(r):
                if r == leng:
                    return row
                row.append(temp[r] + temp[r+1])
                return recurtiontemp(r+1)
            
            row = recurtiontemp(r)
           
          
            pascalTriangle=row
            
            return recursion(rowIndex-1)
       
    
        recursion(rowIndex)
        return pascalTriangle
        