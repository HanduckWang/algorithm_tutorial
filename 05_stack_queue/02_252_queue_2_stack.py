from collections import deque
# python中栈使用list实现，队列可使用deque（双端队列）实现
class MyStack:
    def __init__(self):
        self.que = deque()

    def push(self, x: int) -> None:
        self.que.append(x)

    def pop(self) -> int:
        if self.empty():
            return None

        for i in range(len(self.que) - 1):
            self.que.append(self.que.popleft())  # 将前面size-1个取出放到右边
        return self.que.popleft()

    def top(self) -> int:
        if self.empty():
            return None
        return self.que[-1]

    def empty(self) -> bool:
        return not self.que