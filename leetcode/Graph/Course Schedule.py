# topological sort

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
