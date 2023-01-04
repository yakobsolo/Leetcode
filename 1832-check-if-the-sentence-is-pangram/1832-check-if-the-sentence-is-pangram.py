class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        lett = {}
        for i in sentence:
            lett[i] = 1+lett.get(i, 0)
        if len(lett) >= 26:
            return True
        return False
        