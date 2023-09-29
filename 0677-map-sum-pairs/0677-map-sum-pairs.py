class TrieNode:
    def __init__(self):
        self.children  = [None]*26
        self.isEndofWord = False
        self.count= 0
        
        
class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.dict= defaultdict()
#     def search(self, word: str) -> bool:
#         cur = self.root
#         for w in word:
#             idx = ord(w)-ord("a")
#             if cur.children[idx]!=None:
#                 cur= cur.children[idx]
#             else: return False
            
#         return cur.isEndofWord
                
    def insert(self, key: str, val: int) -> None:
        cur = self.root
        
        if key in self.dict:
            prev_val = self.dict[key]
            for w in key:
                idx = ord(w)-ord('a')
                if cur.children[idx] == None:
                    cur.children[idx] = TrieNode()

                cur  = cur.children[idx]
                cur.count += val-prev_val
            cur.isEndofWord = True 
            self.dict[key] = val
        else:
            for w in key:
                idx = ord(w)-ord('a')
                if cur.children[idx] == None:
                    cur.children[idx] = TrieNode()

                cur  = cur.children[idx]
                cur.count += val
            cur.isEndofWord = True
            self.dict[key] = val
    def sum(self, prefix: str) -> int:
        cur = self.root
        for w in prefix:
            idx = ord(w)-ord("a")
            if cur.children[idx]!=None:
                cur= cur.children[idx]
                
            else: return 0
        return cur.count


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)