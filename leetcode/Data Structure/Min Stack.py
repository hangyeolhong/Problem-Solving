class MinStack(object):
    def __init__(self):
        self.st = []
        
    def push(self, x):
        self.st.append((x, min(self.getMin(), x)))  # tuple
           
    def pop(self):
        self.st.pop()

    def top(self):
        if self.st:
            return self.st[-1][0]
        
    def getMin(self):
        if self.st:
            return self.st[-1][1]
        return 2 ** 31 - 1           
