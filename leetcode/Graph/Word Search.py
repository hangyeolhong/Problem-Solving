class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board),len(board[0]) 
        

        def helper(visited, i, j, count):
            if i < 0 or i > rows - 1 or j < 0 or j > cols - 1 or visited[i][j] or board[i][j] != word[count]:
                return False 

            if count == len(word)-1:
                return True 


            visited[i][j] = True

            d = helper(visited, i + 1, j, count + 1) 
            u = helper(visited, i - 1, j, count + 1)
            r = helper(visited, i, j + 1, count + 1) 
            l = helper(visited, i, j - 1, count + 1)

            visited[i][j] = False

            return d or u or r or l


        visited = [[False] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols): 
                if helper(visited, i, j, 0):
                    return True

        return False   
