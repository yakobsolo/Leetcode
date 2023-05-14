class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        import heapq
        heap = []
        leng1 = len(nums1)
        leng2 = len(nums2)
        
        for i in range(leng1):
            for j in range(leng2):
                temp = nums1[i] + nums2[j]
                
                if len(heap) < k: heapq.heappush(heap, (-temp, (nums1[i], nums2[j])))
                elif -temp > heap[0][0]: heapq.heapreplace(heap, (-temp, (nums1[i], nums2[j])))
                else:
                    break
        
        ans = []
        
        while heap:
            top = heap.pop()
            ans.append((top[1]))
        return ans