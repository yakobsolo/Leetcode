class TrieNode:
    def __init__(self):
        self.children  = [None]*26
        self.isEndofWord = False
            
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    
    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            idx = ord(w)-ord('a')
            if cur.children[idx] == None:
                cur.children[idx] = TrieNode()
                
            cur  = cur.children[idx]
        cur.isEndofWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for w in word:
            idx = ord(w)-ord("a")
            if cur.children[idx]!=None:
                cur= cur.children[idx]
            else: return False
            
        return cur.isEndofWord
                
                
    # def startsWith(self, prefix: str) -> bool:
    #     cur = self.root
    #     for w in prefix:
    #         idx = ord(w)-ord("a")
    #         if cur.children[idx]!=None:
    #             cur= cur.children[idx]
    #         else: return False
    #     return True
            
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dic = Trie()
        for word in wordDict:
            dic.insert(word)
        N= len(s)
        memo = {}
        def dp(S, idx):
            if idx == N:
                if dic.search(S):
                    return True
                return False
                
                
            cur = S+s[idx]
            
            if (cur, idx) in memo:
                return memo[(cur, idx)]
            
            if dic.search(cur):
                if dp("", idx+1):
                    memo[(cur, idx)] = True
                    return memo[(cur, idx)]
            memo[(cur, idx)] = dp(cur, idx+1)     
            return memo[(cur, idx)]
        return dp("", 0)
                
                