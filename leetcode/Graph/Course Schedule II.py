#1. topological sort
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        answer = []

        indegree = [0] * numCourses
        edges = [[] for _ in range(numCourses)] 

        for i in range(len(prerequisites)):
            a, b = prerequisites[i]
            indegree[a] += 1
            edges[b].append(a)  # b -> a

        q = deque()

        # insert node with zero indegree into queue
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:
            x = q.popleft()
            answer.append(x)

            for neighbor in edges[x]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return answer if len(answer) == numCourses else []

#2. dfs
from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = defaultdict(list)

        for crs, pre in prerequisites:
            preMap[pre].append(crs)

        output = []
        visited, cycle = set(), set()

        def dfs(cur_crs):
            if cur_crs in cycle:
                return False
            if cur_crs in visited:
                return True

            cycle.add(cur_crs)
            for next_crs in preMap[cur_crs]:
                if not dfs(next_crs):
                    # if it's cycle
                    return False
            cycle.remove(cur_crs)
            visited.add(cur_crs)
            output.append(cur_crs)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
                
        return output[::-1]
