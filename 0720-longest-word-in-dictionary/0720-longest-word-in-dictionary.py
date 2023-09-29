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
    
class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        dictionary = Trie()
        mx, mx_word= 0, ""
        print(words)
        for word in words:
            n = len(word)
            
            if n==1:
                dictionary.insert(word)
                if mx==0:
                    mx_word = word
                    mx = n
            else:
                if dictionary.search(word[:-1]):
                    # print(word, mx, mx_word)
                    if n>mx:
                        mx_word = word
                        mx = n
                    dictionary.insert(word)
        return mx_word
                
                    
                
        