### Python solution
```python

#1. topological sort O(V + E)

from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        course = [[] for _ in range(numCourses)]
        q = deque()

        for pre in prerequisites:
            a, b = pre
            course[b].append(a)
            indegree[a] += 1

        for c, v in enumerate(indegree):
            if v == 0:
                q.append(c)

        cnt = 0
        while q:
            cur = q.popleft()
            for neighbor in course[cur]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
            cnt += 1
            
        return cnt == numCourses

#2. dfs

from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        visited = set()
        
        for crs, pre in prerequisites:
            preMap[pre].append(crs)

        def dfs(cur_crs):
            if cur_crs in visited:
                return False
              
            if preMap[cur_crs] == []:
                # can finish all course
                return True

            visited.add(cur_crs)
            for next_crs in preMap[cur_crs]:
                if not dfs(next_crs):
                    return False
            visited.remove(cur_crs) # for search from other starting node
            # trick for efficiency
            preMap[cur_crs] = []    # do not double check route starting with cur_crs

            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
```

### Drawing explanation
<img src="https://user-images.githubusercontent.com/59331040/222731731-6377cfe6-f925-47dd-a3a2-4a78029200db.PNG" width="70%">
