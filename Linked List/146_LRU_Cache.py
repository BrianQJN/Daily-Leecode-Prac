"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Example:Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
"""
class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev = self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {} # format: {key: node}

        # left means the least used, right means the recently used
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    # remove node from list
    def remove(self, node):
        """
        :type node: Node
        :rtype: None
        """
        # remove a node from the list, we need to point the last node to the next node
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    # insert node at right
    def insert(self, node):
        """
        :type node: Node
        :rtype: None
        """
        # insert a node at the right, we need to point the previous node of right to the new node, and new node to the right
        prev, next = self.right.prev, self.right
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # get from cache if key exists, else return -1
        # since if the key exists, we need to update the linked list status
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        
        return -1
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]