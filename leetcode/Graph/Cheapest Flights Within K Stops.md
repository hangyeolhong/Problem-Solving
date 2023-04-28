### Python solution
```python
#1. Bellman-Ford O(E*k)

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = int(1e9)
        prices = [INF] * n
        prices[src] = 0

        for i in range(k + 1):
            tmpPrices = prices.copy()

            for s, d, p in flights:  # s=source, d=dest, p=price
                if prices[s] == INF:
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
            
        return -1 if prices[dst] == INF else prices[dst]
        
#2. Dijkstra
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float('inf')] * n
        dist[src] = 0   # starting point
        graph = [[] for _ in range(n)]

        for frm, to, price in flights:
            graph[frm].append((to, price))

        q = deque()
        answer = float('inf')

        q.append((0, src, -1))

        while q:
            cost, cur, stop = q.popleft()
            print(cost, cur, stop, dist)

            if cur == dst and stop <= k:
                answer = min(answer, cost)
            
            for neigh, price in graph[cur]:
                new_cost = cost + price
                if new_cost < dist[neigh]:
                    dist[neigh] = new_cost
                    q.append((new_cost, neigh, stop + 1))

        return -1 if answer == float('inf') else answer
```

### Explanation
- original bellman-ford
- WHY ```tmpPrices = prices.copy()```? because we have to visit only **k** stops
```python
def bellman-ford(start):
    dist = [INF] * (V + 1)
    dist[start] = 0
    for i in range(V):
        for s, d, w in edges:
            if dist[s] != INF and dist[d] > dist[s] + w:
                if i == V - 1:
                    return -1
                dist[d] = dist[s] + w
    return dist    
```
