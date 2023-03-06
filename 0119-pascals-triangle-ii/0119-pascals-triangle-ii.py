class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascalTriangle = [[1]]
        if rowIndex == 0:
            return [1]
        
        for i in range(rowIndex):
            temp = [0]+pascalTriangle[-1]+[0]
            row = []
            
            for j in range(len(temp)-1):
                row.append(temp[j]+temp[j+1])   
            if len(row) == rowIndex+1:
                return row
            pascalTriangle.append(row)
       
        