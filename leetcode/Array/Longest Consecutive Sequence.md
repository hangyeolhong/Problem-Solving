### Python solution
```python
#1. Hash: 331ms
# O(n), O(n)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        total = set(nums)
        answer = 0

        for num in nums:
            if num - 1 not in total:
                # first element
                res = 1
                while num + 1 in total:
                    num += 1
                    res += 1
                
                answer = max(answer, res)

        return answer
            
#2. Union-Find: 621ms
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
```

### Explanation
- Hash: ```set()```
    - We can search value O(1)
    - Check whether ```num``` is the first element of consecutive sequence by ```if num - 1 not in total```
    - Increase sequence length by checking whether next value is in set (```while num + 1 in total```)
