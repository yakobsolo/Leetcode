class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_word = 0
        for sentence in sentences:
            max_word = max(max_word, sentence.count(" ")+1)
        return max_word