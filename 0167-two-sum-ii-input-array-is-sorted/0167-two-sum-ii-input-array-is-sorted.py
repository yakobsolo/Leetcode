class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r=len(numbers)-1
        indexes = []
        while l<r:
            while l<r and numbers[l]+numbers[r] > target:
                r-=1
                
            
            while l<r and numbers[l] +numbers[r] < target:
                l+=1
               
            if numbers[l] +numbers[r] == target:
                indexes.append(l+1)
                indexes.append(r+1)
                print(2)
                return indexes