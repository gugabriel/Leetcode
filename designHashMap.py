"""
Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

    put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
    get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
    remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.




    1). hash function design: the purpose of hash function is to map a key value to an address in the storage space, similarly to the system that we assign a postcode to each mail address. As one can image, for a good hash function, it should map different keys evenly across the storage space, so that we don't end up with the case that the majority of the keys are concentrated in a few spaces.

    2). collision handling: essentially the hash function reduces the vast key space into a limited address space. As a result, there could be the case where two different keys are mapped to the same address, which is what we call 'collision'. Since the collision is inevitable, it is important that we have a strategy to handle the collision.

    for collision, use a bucket at that index to hold multiple values
"""


class ListNode:
    def __init__(self, key, val):
        self.pair = (key, val)
        self.next = None


class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = 1000
        self.h = [None] * self.m

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        index = key % self.m
        if self.h[index] == None:
            self.h[index] = ListNode(key, value)
        else:
            cur = self.h[index]
            while True:
                if cur.pair[0] == key:
                    cur.pair = (key, value)  # update
                    return
                if cur.next == None:
                    break
                cur = cur.next
            cur.next = ListNode(key, value)

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        index = key % self.m
        cur = self.h[index]
        while cur:
            if cur.pair[0] == key:
                return cur.pair[1]
            else:
                cur = cur.next
        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        index = key % self.m
        cur = prev = self.h[index]
        if not cur:
            return
        if cur.pair[0] == key:
            self.h[index] = cur.next
        else:
            cur = cur.next
            while cur:
                if cur.pair[0] == key:
                    prev.next = cur.next
                    break
                else:
                    cur, prev = cur.next, prev.next