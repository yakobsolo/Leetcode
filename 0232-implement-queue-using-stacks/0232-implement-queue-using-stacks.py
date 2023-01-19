class MyQueue:
    def __init__(self):
        self.lisst = []

    def push(self, x: int) -> None:
        self.lisst.append(x)
        return None
        

    def pop(self) -> int:
        return self.lisst.pop(0)
        

    def peek(self) -> int:
        return self.lisst[0]
        

    def empty(self) -> bool:
        if len(self.lisst) == 0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()