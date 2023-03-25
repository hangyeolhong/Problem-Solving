### Python solution
```python
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        area = []   # number of nodes
        visited = set()
        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)


        def dfs(i):
            nonlocal res
            if i in visited:
                return

            visited.add(i)
            res += 1
            for neighbor in graph[i]:
                dfs(neighbor)

        for i in range(n):
            if i not in visited:
                res = 0
                dfs(i)
                area.append(res)

        if len(area) == 1: return 0

        answer = 0
        tmp = area[0]
        for i in range(1, len(area)):
            answer += tmp * area[i]
            tmp += area[i]

        return answer
```
