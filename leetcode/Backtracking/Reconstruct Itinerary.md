### Python solution
```python
import copy

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        visited = [False] * len(tickets)
        res = []
        tickets.sort()

        def dfs(cur, depth):
            # print(cur, depth, res)
            if len(res) == len(tickets):
                res.append(cur)
                return True
            
            for idx, info in enumerate(tickets):
                if info[0] == cur and not visited[idx]:
                    visited[idx] = True
                    res.append(info[0])
                    if dfs(info[1], depth + 1):
                        return True
                    res.pop()
                    visited[idx] = False

            return False

        
        dfs("JFK", 0)

        return res
```
