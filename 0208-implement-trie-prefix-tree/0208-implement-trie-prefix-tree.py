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
                
                
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for w in prefix:
            idx = ord(w)-ord("a")
            if cur.children[idx]!=None:
                cur= cur.children[idx]
            else: return False
        return True
            


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)