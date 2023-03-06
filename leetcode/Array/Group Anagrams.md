### Python solution
```python
# Time complexity: O(mnlogn) --- m = len(strs), n = len(s)
# Space complexity: O(mn!) for the worst case, O(m) for the best case

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lst = defaultdict(list)

        for s in strs:
            lst[''.join(sorted(s))].append(s)

        return list(lst.values())
```
