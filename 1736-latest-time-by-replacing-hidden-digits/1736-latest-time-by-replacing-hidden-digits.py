class Solution:
    def maximumTime(self, time: str) -> str:
        ans = ""
        hash = {0:[2], 1:[9, 9, 3], 3:[5], 4:[9]}
        for i in range(5):
            if time[i] == "?":
                if i == 0:
                    if time[1] != "?" and int(time[1])>=4: ans+="1"
                    else:
                        ans +=str(hash[i][0])
                elif i == 1:
                    ans += str(hash[i][int(ans[0])])
                else:
                    ans += str(hash[i][0])
            else: ans +=time[i]
        return ans