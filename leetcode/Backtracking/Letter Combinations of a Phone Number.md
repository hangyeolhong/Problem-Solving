### Python solution
```python
import copy

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {"2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", \
            "7": "pqrs", "8": "tuv", "9": "wxyz"}
        answer = []
        
        def dfs(s, idx):
            if len(s) == len(digits):
                answer.append(copy.deepcopy(s))
                return 
            
            for i in range(idx, len(digits)):
                for j in range(len(d[digits[i]])):

                    dfs(s + d[digits[i]][j], i + 1)
        
        if digits:
            dfs("", 0)
        return answer
```
