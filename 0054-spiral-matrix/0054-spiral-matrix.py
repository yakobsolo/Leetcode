class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        mtx2 = list(zip(*matrix))
        top, left = 0, 0
        bottom , right = len(matrix)-1, len(matrix[0])-1
        flag = 1
        ans = []
        while top<=bottom and left<= right:
            if flag:
                temp = matrix[top]
                temp2 = mtx2[right]
                ans += temp[left:right+1]
                top += 1
                ans += temp2[top: bottom+1]
                right-=1
                
                flag = 0
            else:
                temp = matrix[bottom]
                temp2= mtx2[left]
                temp1 = temp[left: right +1]
                ans+=temp1[::-1]
                
                bottom -=1
                temp22 = temp2[top: bottom+1]
                ans+=temp22[::-1]
                left +=1
                flag = 1
        return ans

