class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        N = len(nums)
        counter_window = defaultdict(int)
        l = 0
        ans = []
        for i in range(N):
            heappush(heap, -nums[i])
        
            counter_window[nums[i]] +=1
            if len(heap)>=k:
                
                mx = -heappop(heap)
                if nums[l] != mx:
                    heappush(heap, -mx)
                   
                if counter_window[mx] >0:
                    ans.append(mx)    
                else: 
                    while counter_window[mx] == 0 :
                        mx = -heappop(heap)
                    ans.append(mx)
                    if nums[l] != mx:
                        heappush(heap, -mx)
                        
                counter_window[nums[l]]-=1
                l+=1
                        
        return ans
                