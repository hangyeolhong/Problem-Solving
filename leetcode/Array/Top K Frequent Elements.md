### Python solution
```python
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        sorted_c = sorted(c.items(), key=lambda x: -x[1])[:k]   # top-k counts

        answer = []
        for num, cnt in sorted_c:
            answer.append(num)

        return answer
```
