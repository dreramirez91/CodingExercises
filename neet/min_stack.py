class MinStack:

    def __init__(self):
        self.stack = []
        # If you want O(1), keep track of it from the beginning, using more memory instead of looping to find it at the end
        self.minimums = [float("inf")]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.minimums[-1]:
            self.minimums.append(val)

    def pop(self) -> None:
        current_min = self.stack.pop()
        if current_min == self.minimums[-1]:
            self.minimums.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self):
        return self.minimums[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
