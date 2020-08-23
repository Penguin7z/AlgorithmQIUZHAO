# -*- coding: utf-8 -*-

import collections

# LRU缓存机制

# 思路总结
# 用有序的dict搞定


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.items = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.items.keys():
            return -1

        value = self.items.pop(key)
        self.items[key] = value
        return value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.items.keys():
            self.items.pop(key)
        else:
            if self.capacity > 0:
                self.capacity -= 1
            else:
                self.items.popitem(last=False)

        self.items[key] = value


if __name__ == "__main__":
    obj = LRUCache(10)

