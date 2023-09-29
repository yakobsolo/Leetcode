class TrieNode:
    def __init__(self):
        self.children  = [None]*26
        self.count = 0
            
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.memo  = {}
    
    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            idx = ord(w)-ord('a')
            if cur.children[idx] == None:
                cur.children[idx] = TrieNode()
                
            cur  = cur.children[idx]
            cur.count+=1

  
    def calcPrefix(self, word: str) -> None:
        if word not in self.memo:
            self.memo[word] = 0
            cur = self.root
            for char in word:
                idx = ord(char)-ord("a")
                cur = cur.children[idx]
                self.memo[word] += cur.count
        return self.memo[word]   
    
    # searching all prefix will be O(N3)
    
    # def startsWith(self, prefix: str) -> bool:
    #     cur = self.root
    #     for w in prefix:
    #         idx = ord(w)-ord("a")
    #         if cur.children[idx]!=None:
    #             cur= cur.children[idx]
    #         else: return 0
    #     return cur.count
            
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.insert(word)
       
        
        ans = [trie.calcPrefix(word) for word in words]
        return ans       
                
        