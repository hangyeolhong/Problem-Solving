# 331ms
# O(n), O(n)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0

        for num in nums:
            if num - 1 in nums:
                # if not the first element of sequence
                continue
                
            tmp_length = 1

            while num + tmp_length in nums:
                tmp_length += 1

            res = max(res, tmp_length)
        return res


      
      
""" union-find: 621ms
from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        def find_parent(parent, x):
            if parent[x] != x:
                parent[x] = find_parent(parent, parent[x])
            return parent[x]


        def union(parent, x, y):
            a = find_parent(parent, x)
            b = find_parent(parent, y)

            parent[a] = b if a < b else parent[b] = a

        nums = set(nums)
        if not nums:
            return 0

        parent = dict()
        for num in nums:
            parent[num] = num

        for num in nums:
            if num - 1 in nums and find_parent(parent, num - 1) != find_parent(parent, num):
                union(parent, num - 1, num)
            if num + 1 in nums and find_parent(parent, num + 1) != find_parent(parent, num):
                union(parent, num + 1, num)
        

        d = defaultdict(list)
        for num in nums:
            d[find_parent(parent, num)].append(num)

        res = sorted(d.values(), key=lambda x: -len(x))
        return len(res[0])
        # return max([len(l) for l in d.values()]) 
        
"""
