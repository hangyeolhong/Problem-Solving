### Python solution
```python
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        a = [(p, s) for p, s in zip(position, speed)]
        a.sort(key=lambda x: -x[0])
        print(a)
        
        st = []
        for p, s in a:
            st.append((target - p) / s)
            if len(st) >= 2 and st[-1] <= st[-2]:
                st.pop()

        return len(st)
```

### Explanation
```
If the car in behind arrives earlier than the car in the stack[-1], they must collide.
```
