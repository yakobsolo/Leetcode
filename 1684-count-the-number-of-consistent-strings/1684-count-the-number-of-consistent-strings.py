class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        n = len(words)
        count = 0
        for i in range(n):
            al = True
            for w in words[i]:
                if w not in allowed: al = False
            if al: count +=1
        return count