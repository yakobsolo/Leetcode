class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
        filename = defaultdict(deque)
        for path in paths:
            temp = list(path.split())
            for i in range(1, len(temp)):
                file = list(temp[i].split("("))
                hash[file[1][:-1]].append(temp[0])
                filename[file[1][:-1]+temp[0]].append(file[0])
        res = []
        for key in hash:
            if len(hash[key]) >1:
                temp = []
                for direc in hash[key]:
                    temp.append(direc+"/"+filename[key+direc][0])
                    filename[key+direc].popleft()
                res.append(temp)
        return res