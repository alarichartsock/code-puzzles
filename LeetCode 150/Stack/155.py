class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:
        if self.min == None:
            self.min = val
        elif self.min > val:
            self.min = val
        self.stack.append(val)

    def pop(self) -> None:
        popped = self.stack[len(self.stack)-1]
        del self.stack[len(self.stack)-1]
        if self.min == popped and len(self.stack) > 0:
            self.min = min(self.stack)
        elif self.min == popped:
            self.min = None
            
    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        return self.min
