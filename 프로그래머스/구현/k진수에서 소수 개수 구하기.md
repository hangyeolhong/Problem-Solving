### Python solution
```python
def check(x):
    if x == 1: return False

    for i in range(2, int(x ** (1 / 2)) + 1):
        if x % i == 0:
            return False
        
    return True


def solution(n, k):
    answer = 0
    res = ""
    
    while n != 0:
        res += str(n % k)
        n //= k
        
    res = res[::-1].split('0')

    for num in res:
        if num:
            if check(int(num)):
                answer += 1
    
    return answer
```
