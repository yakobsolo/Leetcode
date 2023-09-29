class TrieNode:
    def __init__(self):
        self.children  = [None]*26
        self.count = 0
            
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.prefixScores  = {}
    
    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            idx = ord(w)-ord('a')
            if cur.children[idx] == None:
                cur.children[idx] = TrieNode()
                
            cur  = cur.children[idx]
            cur.count+=1

  
    def prefixScore(self, word: str) -> None:
        if word not in self.prefixScores:
            self.prefixScores[word] = 0
            currentNode = self.root
            for char in word:
                idx = ord(char)-ord("a")
                currentNode = currentNode.children[idx]
                self.prefixScores[word] += currentNode.count
        return self.prefixScores[word]        
                
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for w in prefix:
            idx = ord(w)-ord("a")
            if cur.children[idx]!=None:
                cur= cur.children[idx]
            else: return 0
        return cur.count
            
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.insert(word)
       
        
        ans = [trie.prefixScore(word) for word in words]
        return ans       
                
        