class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        convert =  {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        n1, n2 = 0, 0
        
        for i, v in enumerate(num1[::-1]):
            n1 += convert[v] * 10**i
        for i,v in enumerate(num2[::-1]):
            n2 += convert[v] * 10**i
        res = n1*n2
        return str(res)