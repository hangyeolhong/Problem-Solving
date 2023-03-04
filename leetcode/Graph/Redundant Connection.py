# Union-Find

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find_parent(x):
            if parent[x] != x:
                parent[x] = find_parent(parent[x])
            return parent[x]

        def union(x, y):
            x1, y1 = find_parent(x), find_parent(y)

            if x1 == y1:
                return False
            if x1 < y1:
                parent[y1] = x1
            else:
                parent[x1] = y1
            
            return True

        parent = [i for i in range(len(edges) + 1)]

        for a, b in edges:
            if not union(a, b):
                return [a, b]
            
