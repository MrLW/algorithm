class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = 1009
        self.tables = [[] for _ in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        hashKey = self.hash(key)
        if key in self.tables[hashKey]:
            return
        self.tables[hashKey].append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        hashKey = self.hash(key)
        if key not in self.tables[hashKey]:
            return
        self.tables[hashKey].remove(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        hashKey = self.hash(key)
        return key in self.tables[hashKey]


set = MyHashSet()
set.add(1)
set.add(2)
print('contains(1)', set.contains(1))
print('contains(3)', set.contains(3))
set.add(2)
set.remove(2)
print('contains(2)', set.contains(3))
