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
