### Python solution
```python
from collections import defaultdict

class DetectSquares:

    def __init__(self):
        self.d = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.d[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        px, py = point
        answer = 0

        for x, y in self.pts:
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            answer += self.d[(x, py)] * self.d[(px, y)]
        
        return answer

```

### Explanation
- Use hashmap for distinct point (x, y)
- count operation: To become a rectangle, there must be coordinates on the diagonal and coordinates that trade the values of x and y.
    - ```answer += self.d[(x, py)] * self.d[(px, y)]```
