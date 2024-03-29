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
        self.flattenList = [];
        self.__flatten(nestedList)
        self.cur = 0
    
    def __flatten(self, nestedList: [NestedInteger]):
        for l in nestedList:
            if l.isInteger():
                self.flattenList.append(l.getInteger())
            else :
                self.__flatten(l.getList())
        
    
    def next(self) -> int:
        r = self.flattenList[self.cur]
        self.cur += 1
        return r
        
    
    def hasNext(self) -> bool:
        return self.cur < len(self.flattenList)

s = NestedIterator([1, [[2, 3], [4, [5, 6]]]])

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
