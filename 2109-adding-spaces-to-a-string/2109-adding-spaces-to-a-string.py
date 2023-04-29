class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []
        prev=0
        for i in spaces:
            ans.append(s[prev: i])
            ans.append(" ")
            prev=i
        if prev != len(s):
            ans.append(s[prev:])
        else:
            ans.pop()
        return "".join(ans)