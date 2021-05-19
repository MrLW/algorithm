class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._in = list()
        self._out = list()


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self._in.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self._out:
            while self._in:
                self._out.append(self._in.pop())
        return self._out.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        ele = self.pop()
        self._out.append(ele)
        return ele


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self._in and not self._out


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
param_2 = obj.pop()
param_3 = obj.peek()
param_5 = obj.empty()
param_4 = obj.pop()
print('')