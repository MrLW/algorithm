class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.base = 1001
        self.table = [None]*self.base

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        node = Node(key, value)
        hashKey = self.hash(key)
        head = self.table[hashKey]
        if head is None:
            self.table[hashKey] = node
            return
        last = None
        while head is not None:
            if(head.key == key):
                head.value = value
                return
            last = head
            head = head.next
        last.next = node

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        hashKey = self.hash(key)
        head = self.table[hashKey]
        while head is not None:
            if(head.key == key):
                return head.value
            head = head.next
        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        hashKey = self.hash(key)
        head = self.table[hashKey]
        if head is None:
            return
        last = None
        if head.key == key:
            self.table[hashKey] = head.next
            return
        while head is not None:
            if head.key == key:
                last.next = head.next
                return
            last = head
            head = head.next

    def hash(self, key):
        return key % self.base


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


mMap = MyHashMap()
mMap.put(1, 1)
mMap.put(2, 2)
print('1==>', mMap.get(1))
print('2==>', mMap.get(2))
mMap.remove(2)
print('2==>', mMap.get(2))

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
