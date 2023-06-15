class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hash = defaultdict(int)
        for domain in cpdomains:
            if domain.count(".") == 2:
                rep, d = domain.split()
                f, s, t = d.split(".")
                rep = int(rep)
                hash[d]+= rep
                hash[t]+= rep
                hash[s+"."+t] += rep
            else:
                rep, d = domain.split()
                f, s = d.split(".")
                hash[d] += int(rep)
                hash[s] += int(rep)
        ans = []
        for key in hash:
            temp = str(hash[key]) +" "+ key
            ans.append(temp)
        return ans