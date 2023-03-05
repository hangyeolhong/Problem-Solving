### Python solution
```python
# Prim (3.8ms) is faster than Kruskal (5.4ms), because the size of edge set is large.

#1. Kruskal
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def find_parent(x, parent):
            if parent[x] != x:
                parent[x] = find_parent(parent[x], parent)
            return parent[x]
        
        def union(x, y, parent):
            x1 = find_parent(x, parent)
            y1 = find_parent(y, parent)
            if x1 < y1:
                parent[y1] = x1
            else:
                parent[x1] = y1
        
        q = []
        for idx, point in enumerate(points):
            for i in range(idx + 1, len(points)):
                heapq.heappush(q, [abs(points[i][0] - point[0]) + abs(points[i][1] - point[1]), idx, i])
        parent = [i for i in range(len(points))]
        answer = 0
        while q:
            l, x, y = heapq.heappop(q)
            if find_parent(x, parent) != find_parent(y, parent):
                union(x, y, parent)
                answer += l
        return answer

#2. Prim
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i: [] for i in range(N)}  # i : list of [cost, node]
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # Prim's
        res = 0
        visit = set()
        minH = [[0, 0]]  # [cost, point]
        while len(visit) < N:
            cost, i = heapq.heappop(minH)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH, [neiCost, nei])
        return res
```

### Drawing explanation
<img src="https://user-images.githubusercontent.com/59331040/219867821-e7390fbb-0b94-48d5-b33a-24f09457c06d.png" width="70%">
