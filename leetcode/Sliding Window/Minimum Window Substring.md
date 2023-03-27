### Python solution
```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t: return ""

        countS = {}

        # count each character of t
        countT = {}
        for ch in t:
            countT[ch] = 1 + countT.get(ch, 0)
        
        have, need = 0, len(countT) # unique character
        l = 0
        res = [-1, -1]
        answer = 1e5 + 1
        
        for r, ch in enumerate(s):
            # count each character of s
            countS[ch] = 1 + countS.get(ch, 0)

            if ch in countT and countS[ch] == countT[ch]:
                have += 1

            while have == need:
                # update minimum window substring
                if r - l + 1 < answer:
                    answer = r - l + 1
                    res = [l, r]

                # move left pointer
                countS[s[l]] -= 1
                
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r + 1]
```
