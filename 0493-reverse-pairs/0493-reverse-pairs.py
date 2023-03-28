class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(left, right):
            ll, lr = 0, 0
            leng1 , leng2 = len(left), len(right)
            merged = []
            while ll<leng1 and lr < leng2:
                if left[ll] <= right[lr]:
                    merged.append(left[ll])
                    ll+=1
                elif right[lr] < left[ll]:
                    merged.append(right[lr])
                    lr +=1
            
            while ll<leng1:
                merged.append(left[ll])
                ll+=1
            while lr< leng2:
                merged.append(right[lr])
                lr +=1
            
            return merged
        
        self.rp = 0
        left, right = 0, len(nums)-1
        def mergesort(left, right):
            if left == right:
                return [nums[left]]
            
            mid = left + (right-left)//2
            
            leftmerge = mergesort(left, mid)
            rightmerge = mergesort(mid+1,right)
            
            l, r = 0, 0
            leng1 , leng2 = len(leftmerge), len(rightmerge)
            while l<leng1 and r< leng2:
                if leftmerge[l]> rightmerge[r]*2:
                    self.rp +=1
                    r +=1
                else:
                    l+=1
                    if l<leng1:
                        self.rp+=r
            l+=1
            while l< leng1:
                self.rp +=r
                l+=1
            return merge(leftmerge, rightmerge)
        
        merged = mergesort(left, right)
        
        return self.rp 