class MinStack:

    def __init__(self):
        self.q = list()
        self.min = float('inf')
        

    def push(self, val: int) -> None:
        if not self.q:
            self.q.append(0)
            self.min = val
        else:
            self.q.append(val - self.min)
            if val < self.min:
                self.min = val
        

    def pop(self) -> None:
        if not self.q:
            return

        pop = self.q.pop()

        if pop < 0:
            self.min = self.min - pop
        

    def top(self) -> int:
        top = self.q[-1]
        if top > 0:
            return top + self.min
        else:
            return self.min
        

    def getMin(self) -> int:
        return self.min
        
