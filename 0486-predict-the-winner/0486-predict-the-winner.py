class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        l = 0
        r= len(nums) -1
        t = True
        # if r == 0:
        #     return True
        
        def predict(l, r, t):
            if l>r:
                return 0
            
            if t:
                return max(nums[l] + predict(l+1, r, not t), nums[r]+predict(l, r-1, not t))
            else:
                return min(-nums[l] + predict(l+1, r, not t), -nums[r] + predict(l, r-1, not t))
        
        if predict(l, r, t) >= 0:
            return True
        else:
            return False
                
        
#         player1 , player2 = [], []
#         flag = 1
#         l = 0
#         r = len(nums) -1
#         def predict(l, r):
#             nonlocal flag
            
#             if l>r:
#                 return True
#             # if sum(player1) > sum(player2):
#             #         return True
               
#             if flag:
#                 print(l)
#                 player1.append(nums[l])
#                 print(player1, player2)
#                 print("----------")
#                 flag = 0
#                 left = predict(l+1, r)
                
#                 if sum(player1) > sum(player2):
#                     return True
              
#                 player1.pop()
#                 right =  predict(l, r-1)
#                 return left and right
#             else:
#                 player2.append(nums[l])
#                 print(player2,player1)
#                 print(l)
#                 flag = 1
#                 left = predict(l+1, r)
                
#                 if sum(player1) > sum(player2):
#                     return True
#                 player2.pop()
#                 right = predict(l, r-1)
#                 return left and right
#         return predict(l, r)