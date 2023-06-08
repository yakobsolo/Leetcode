class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner = defaultdict(int)
        losser = defaultdict(int)
        for w, l in matches:
            winner[w]+=1
            losser[l] +=1
        ans = []
        temp = []
        for key in winner:
            if key not in losser: temp.append(key)
        temp.sort()
        ans.append(temp)
        temp = []
        for key in losser:
            if losser[key] == 1: temp.append(key)
                
        temp.sort()
        ans.append(temp)
        return ans