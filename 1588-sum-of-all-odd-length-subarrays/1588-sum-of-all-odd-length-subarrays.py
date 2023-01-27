class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sums= 0
        l = 0
        r = 0
        number_subarrays = 0
        odd_subarrays = 0
        for i in range(len(arr)):
            l = i+1
            r = len(arr) -i
            number_subarrays = l * r
            if number_subarrays%2 == 0:
                odd_subarrays = number_subarrays //2
            else: 
                odd_subarrays = number_subarrays//2+1
            sums += odd_subarrays* arr[i]
        return sums
                
            