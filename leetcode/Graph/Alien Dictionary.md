### Python solution
```python
#1. topological sort
from collections import deque

words = ["wrt", "wrf", "er", "ett", "rftt"]  # already sorted
q = deque()
indegree = {}
graph = {}

for word in words:
    for c in word:
        indegree[c] = 0
        graph[c] = set()  # avoid duplication

for i in range(len(words) - 1):
    mn = min(len(words[i]), len(words[i + 1]))

    for k in range(mn):
        # check the first different characters
        if words[i][k] != words[i + 1][k]:
            graph[words[i][k]].add(words[i + 1][k])
            break

for char, s in graph.items():
    for c in s:
        indegree[c] += 1

for char, in_cnt in indegree.items():
    if not in_cnt:
        q.append(char)

res = ""
while q:
    w = q.popleft()
    res += w

    for i in graph[w]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

print(res)


#2. post order dfs
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {char: set() for word in words for char in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    print(w1[j], w2[j])
                    adj[w1[j]].add(w2[j])
                    break

        visited = {}  # {char: bool} False visited, True current path
        res = []

        def dfs(char):
            if char in visited:
                # already visited
                # True: duplicated
                # False: normally completed
                return visited[char]

            visited[char] = True

            for neighChar in adj[char]:
                if dfs(neighChar):
                    return True

            visited[char] = False
            res.append(char)

        for char in adj:
            if dfs(char):
                return ""

        res.reverse()
        return "".join(res)
```

### Explanation
```
1. Key of the indegree and graph consists only of words that appear in the words.
  * No other lower case alphabetic characters required
2. When representing graph connections, use set to prevent duplication
```
