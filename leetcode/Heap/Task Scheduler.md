### Python solution
```python
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # [-cnt, idletime]
        
        while maxHeap or q:
            time += 1

            if maxHeap:
                # pop the most frequent task
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
                
        return time
```

### Explanation
- **Two data structures** are needed
  - 1. **Maxheap** for finding the most frequent tasks
  - 2. **Queue** for recording the number of tasks remaining and cool down time  & popping the task that went in first
