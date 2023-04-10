### Python solution
```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for t in tokens:
            if t == '+':
                st.append(st.pop() + st.pop())
            elif t == '-':
                y = st.pop()
                x = st.pop()
                st.append(x - y)
            elif t == '*':
                st.append(st.pop() * st.pop())
            elif t == '/':
                y = st.pop()
                x = st.pop()
                st.append(int(x / y))
            else:
                st.append(int(t))

        return st[0]
```

### Explanation
- ```str.isnumeric()```: only considers integer greater than zero
- Therefore, reorder if-else condition statements so that symbols are processed first, and then rest integers including negative values are processed.
- negative division: ```int(x / y)```
