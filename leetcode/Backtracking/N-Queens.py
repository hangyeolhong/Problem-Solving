class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.col = [0] * n
        self.answer = []

        self.n_queens(0)

        return self.answer
        
    
    def is_promising(self, x):
        for i in range(x):
            if self.col[i] == self.col[x] or abs(self.col[i] - self.col[x]) == abs(i - x):
                return False
        return True


    # check xth columns
    def n_queens(self, x):
        if x == self.n:
            result = []

            for pos in self.col:
                result.append('.' * pos + 'Q' + '.' * (self.n - 1 - pos))

            self.answer.append(result)
            return


        for i in range(self.n):
            self.col[x] = i             # place queen on (i, x)
            if self.is_promising(x):
                self.n_queens(x + 1)    # check next columns
