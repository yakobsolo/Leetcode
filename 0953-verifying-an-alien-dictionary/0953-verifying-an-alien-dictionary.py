class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ordd= {ch:i for i , ch in enumerate(order)}
        wordnum = list()
        for word in words:
            tmp = []
            for w in word:
                tmp.append(ordd[w])
            wordnum.append(tmp)
        
        for i in range(1, len(words)):
            if wordnum[i-1] > wordnum[i]: return False
        return True