### Python solution
```python
#1.
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []

        def dfs(opn, close, res):
            if len(res) == 2 * n:
                answer.append(res)  # don't have to deep copy (res[::]) because string is immutable
                return

            if close < opn and close < n:
                dfs(opn, close + 1, res + ")")
            if opn < n:
                dfs(opn + 1, close, res + "(")

        dfs(0, 0, "")

        return answer
        
#2.
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []

        def dfs(open_, close_, res, idx):
            if open_ < close_:
                return

            if idx == 2 * n:
                answer.append(res[:])
                return

            if open_ < n:
                dfs(open_ + 1, close_, res + "(", idx + 1)
            dfs(open_, close_ + 1, res + ")", idx + 1)

        dfs(0, 0, "", 0)

        return answer
```
