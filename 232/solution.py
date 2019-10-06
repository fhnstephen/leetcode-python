class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._list = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self._list.insert(0, x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        tmp = []
        while len(self._list) != 0:
            print(tmp, self._list)
            tmp.append(self._list.pop(0))
            print(tmp, self._list)
        result = tmp.pop()
        while len(tmp) != 0:
            self._list.insert(0, tmp.pop())
        return result

    def peek(self) -> int:
        """
        Get the front element.
        """
        tmp = []
        while len(self._list) != 0:
            tmp.append(self._list.pop(0))
        result = tmp[0]
        while len(tmp) != 0:
            self._list.insert(0, tmp.pop())
        return result

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self._list) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()