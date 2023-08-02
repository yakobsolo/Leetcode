class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(r):
            l = 0
            while l<r:
                arr[l], arr[r] = arr[r], arr[l]
                l+=1
                r-=1
            
        n = len(arr)
        ans = []
        for i in range(n-1, -1, -1):
            right = i
            for j in range(i, -1, -1):
                if arr[j] > arr[right]: right = j
            if right != i:
                flip(right)
                flip(i)
                ans.append(right+1)
                ans.append(i+1)
        return ans