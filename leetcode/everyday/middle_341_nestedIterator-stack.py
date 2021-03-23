# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        pass

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        pass

    def getList(self) -> [NestedInteger]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        pass


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = nestedList

    def next(self) -> int:
        ret = self.stack[0]
        del self.stack[0]
        return ret

    def hasNext(self) -> bool:
        while len(self.stack):
            if self.stack[0].isInteger():
                return
            else:
                cur = self.stack[0].getList()

                del self.stack[0]

                self.stack = cur + self.stack
                

s = NestedIterator([1, [[2, 3], [4, [5, 6]]]])

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
