### Python solution
```python

import heapq
from collections import defaultdict
# Dijkstra algorithm keeps the shortest distance array "dist"


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = int(1e9)
        dist = [INF] * n    # one-indexed
        dist[k - 1] = 0     # start point

        # directed edges
        adj = defaultdict(list)

        for time in times:
            u, v, w = time
            adj[u - 1].append([v - 1, w])

        q = []
        heapq.heappush(q, [0, k - 1])   # [dist, zero-indexed node number]

        while q:
            d, cur = heapq.heappop(q)

            if dist[cur] < d:
                continue

            for neighbor, cost in adj[cur]:
                if cost + d < dist[neighbor]:
                    dist[neighbor] = cost + d
                    heapq.heappush(q, [dist[neighbor], neighbor])

        return -1 if INF in dist else max(dist)
```
