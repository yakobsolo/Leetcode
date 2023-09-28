class TrieNode:
    def __init__ (self):
        self.children = [None]*26
        self.isEndofWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            idx = ord(w)-ord('a')
            if cur.children[idx] == None:
                cur.children[idx] = TrieNode()
                
            cur  = cur.children[idx]
        cur.isEndofWord = True
        

    def search(self, word: str) -> bool:
        cur = self.root
        def dfs(i, cur):
            if i >= len(word):
                return cur.isEndofWord
            if word[i] == ".":
                flag = False
                for j in range(26):
                    if cur.children[j]:
                        if dfs(i + 1,cur.children[j]):
                            return True
            else:
                if not cur.children[ord(word[i]) - ord("a")]:
                    return False
                return dfs(i + 1,cur.children[ord(word[i]) - ord("a")])
        return dfs(0, cur)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)