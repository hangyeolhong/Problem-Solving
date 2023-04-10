### Python solution
```python
def solution(N, number):
def solution(N, number):
    answer = 0
    dp = [[] for _ in range(9)]
    
    for i in range(1, 9):
        s = set()
        s.add(int(str(N) * i))
    
        for j in range(1, i):
            for op1 in dp[j]:
                for op2 in dp[i - j]:
                    s.add(op1 + op2)
                    s.add(op1 - op2)
                    s.add(op1 * op2)
                    if op2 != 0:
                        s.add(op1 // op2)
                    
        if number in s:
            return i
        
        dp[i] = s
        
    return -1
```

### Explanation
- dp[i] = N을 i번 써서 만들 수 있는 수의 집합
- 매 i마다, dp[j]와 dp[i - j]의 조합으로 만들 수 있는 수를 구해서 dp[i]에 업뎃해줌
- 예) i==3, dp[1] & dp[2], dp[2] & dp[1]의 조합
