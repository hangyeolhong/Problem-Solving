### Python solution
```python
class MinStack:

    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        if not self.st:
            self.st.append((val, val))
        else:
            mn = self.st[-1][1]
            if val < mn:
                self.st.append((val, val))
            else:
                self.st.append((val, mn))

    def pop(self) -> None:
        self.st.pop()
        

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]
```
