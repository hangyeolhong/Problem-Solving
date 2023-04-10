### Python solution
```python
#1.
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
        
#2. 
class MinStack:

    def __init__(self):
        self.st = []
        self.min_st = []    # record the minimum value before the current index

    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.min_st:
            self.min_st.append(val)

        else:
            if val < self.min_st[-1]:
                self.min_st.append(val)
            else:
                self.min_st.append(self.min_st[-1])
        
    def pop(self) -> None:
        self.st.pop()
        self.min_st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.min_st[-1]

```
