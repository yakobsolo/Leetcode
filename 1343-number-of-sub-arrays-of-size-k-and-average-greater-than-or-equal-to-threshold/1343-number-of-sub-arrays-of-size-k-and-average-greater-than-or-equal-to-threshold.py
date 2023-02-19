class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sums, avg = 0, 0
        l, r = 0, 0
        count =0 
        while r < len(arr):
            sums += arr[r]
            if r>= k-1:
                avg = sums/k
                if avg >= threshold:
                    count +=1 
                sums -= arr[l]
                l+=1
            r +=1
        return count
       