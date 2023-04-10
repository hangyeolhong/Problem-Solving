### Python solution
```python
class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        
        closeToOpen = {')' : '(', '}' : '{', ']': '['}

        for i in range(len(s)):
            if s[i] in closeToOpen:
                # close bracket
                if st and st[-1] == closeToOpen[s[i]]:
                    st.pop()
                else:
                    return False
            else:
                st.append(s[i]) # open bracket

        return True if not st else False
```
