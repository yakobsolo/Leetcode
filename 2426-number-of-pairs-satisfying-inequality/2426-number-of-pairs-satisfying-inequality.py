class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
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
        
        self.npsi = 0
        left, right = 0, len(nums1)-1
        comb = []
        for i in range(right+1):
            comb.append(nums1[i] - nums2[i])
            
        def mergesort(left, right):
            if left == right:
                return [comb[left]]
            
            mid = left + (right-left)//2
            
            leftmerge= mergesort(left, mid)
            rightmerge= mergesort(mid+1,right)
                        
            l, r = 0, 0
            leng1 , leng2 = len(leftmerge), len(rightmerge)
            while l < leng2 and r < leng1:
                if rightmerge[l] >= leftmerge[r]-diff:
                    self.npsi += 1
                    r += 1
                else:
                    l+=1
                    if l < leng2:
                        self.npsi+=r
                        
            l+=1
            while l< leng2:
                self.npsi += r
                l+=1
            
            return merge(leftmerge, rightmerge)
              
        mergesort(left, right)
        return self.npsi 