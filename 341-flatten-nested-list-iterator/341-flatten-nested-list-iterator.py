# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.ans = []
        self.pointer = 0
        for i in nestedList:
            self.getNested(i)
        
    def next(self) -> int:
        self.pointer += 1
        return self.ans[self.pointer-1]
    
    def hasNext(self) -> bool:
        if self.pointer == len(self.ans):
            return False
        return True
            
    def getNested(self, l):
        try:
            for i in l:
                self.getNested(i)
        except:
            if l.isInteger():
                self.ans.append(l.getInteger())
                return
            self.getNested(l.getList())
        
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())