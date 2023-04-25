### Python solution
```python
class TrieNode:
    def __init__(self):
        self.children = {}  # children['a'] = TrieNode()
        self.endOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root

        for w in word:
            if w not in cur.children:
                return False
            cur = cur.children[w]

        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for w in prefix:
            if w not in cur.children:
                return False
            cur = cur.children[w]
        
        return True
```

### Explanation
- We can use HashMap, but ```startsWith``` is the problem. Therefore, we have to use a datastructure, Trie.
- Using Trie, we can search word with ```O(n)```, where n is the length of the longest word.
- Time complexity of ```insert``` is ```O(mn)```, where m is the number of words.
