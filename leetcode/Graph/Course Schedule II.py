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


        if len(answer) == numCourses:
            return answer
        else:
            return []   # empty array    
