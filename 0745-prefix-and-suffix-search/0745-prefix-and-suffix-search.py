class TrieNode:
    def __init__(self):
        self.children = {}
        self.ind = -1
        self.end = False 

class WordFilter:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for j,word in enumerate(words):
            node = self.root
            for i in word:
                if i not in node.children:
                    node.children[i] = TrieNode()
                node = node.children[i]
            node.ind = j
            node.end = True

    def f(self, pref: str, suff: str) -> int:
        node = self.root
        for i in pref:
            if i not in node.children:
                return -1
            node = node.children[i]
        ind = -1
    
        def dfs(node,word):
            nonlocal ind
            if node.end:
                if word[len(word) - len(suff):] == suff:
                    ind = max(ind,node.ind)
            for i in node.children:
                dfs(node.children[i],word + i)
        dfs(node,pref)
        return ind