### Python solution
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]

        cur.endOfWord = True
        
    def search(self, word: str) -> bool:

        def dfs(idx, root):
            cur = root

            for i in range(idx, len(word)):
                c = word[i]
                if c == '.':
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                    
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]

            return cur.endOfWord

        return dfs(0, self.root)
```

### Explanation
```
for child in cur.children.values():
    if dfs(i + 1, child):
        return True
    else: 
        return False
```
- The above is wrong because ```a.``` return ```cur.endOfWord```, which is True.
- If there are remaining characters, and the current node has no children or there are no matching cases, it should return False.
```
for child in cur.children.values():
    if dfs(i + 1, child):
        return True
return False
```
