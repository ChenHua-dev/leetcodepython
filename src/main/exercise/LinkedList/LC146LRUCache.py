class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.least = None
        self.most = None

    def insert_most(self, key: int, value: int) -> None:
        curr = Node(value)
        self.cache[key] = curr
        curr.prev = self.most
        if not self.most:  # most is None and least is None
            self.least = curr
        else:
            self.most.next = curr
        self.most = curr
        # if self.most is not None and self.least is not None:
        #     curr.prev = self.most
        #     curr.prev.next = curr
        #     self.most = curr
        # elif self.most is not None and self.least is None:
        #     curr.prev = self.most
        #     curr.prev.next = curr
        #     self.least = curr.prev
        #     self.most = curr
        # else:  # if not self.most and not self.least:
        #     self.most = curr

    def remove(self, key: int) -> None:
        curr = self.cache.get(key)
        if not curr.prev and not curr.next:
            self.least = None
            self.most = None
        elif not curr.next:
            self.most = curr.prev
            self.most.next = None
            curr.prev = None
        elif not curr.prev:
            self.least = curr.next
            self.least.prev = None
            curr.next = None
        else:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            curr.prev = None
            curr.next = None
        self.cache.pop(key)

    def get(self, key: int) -> int:
        if key in self.cache:
            temp_val = self.cache[key].val
            self.remove(key)
            self.insert_most(key, temp_val)
            temp_node = self.cache[key]
            return temp_node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(key)

        if len(self.cache) >= self.cap:
            key_to_evict = -1
            for item in self.cache.items():
                if item[1] == self.least:
                    key_to_evict = item[0]
                    break
            self.remove(key_to_evict)
        self.insert_most(key, value)
        # if len(self.cache) < self.cap:
        #     if key in self.cache:
        #         self.remove(key)
        # else:
        #     if key in self.cache:
        #         self.remove(key)
        #     else:
        #         key_to_evict = -1
        #         for item in self.cache.items():
        #             if item[1] == self.least:
        #                 key_to_evict = item[0]
        #                 break
        #         self.remove(key_to_evict)
        # self.insert_most(key, value)
        # if len(self.cache) < self.cap:
        #     if key not in self.cache:
        #         self.insert_most(key, value)
        #     else:
        #         self.remove(key)
        #         self.insert_most(key, value)
        # else:
        #     if key not in self.cache:
        #         key_to_evict = -1
        #         for item in self.cache.items():
        #             if item[1] == self.least:
        #                 key_to_evict = item[0]
        #                 break
        #         self.remove(key_to_evict)
        #         self.insert_most(key, value)
        #     else:
        #         self.remove(key)
        #         self.insert_most(key, value)


if __name__ == '__main__':
    # Test case 5
    lru = LRUCache(2)
    print(lru.get(2))     #  return -1
    lru.put(2, 6)  # cache is {2=6}
    print(lru.get(1))     #  return -1
    lru.put(1, 5)  #  LRU key was 2, evicts key 2, cache is {2=6, 1=5}
    lru.put(1, 2)  #  LRU key was 2, evicts key 2, cache is {2=6, 1=2}
    print(lru.get(1))     #  returns 2 (not found)
    print(lru.get(2))     #  returns 6 (not found)

    # # Test case 4:
    # lru = LRUCache(2)
    # lru.put(2, 1)  # cache {2=1}
    # lru.put(2, 2)  #  cache {2=2} b/c need to update the value for the key
    # print(lru.get(2))     #  return 2, cache is {2=1}
    # lru.put(1, 1)  #  LRU key was 2, evicts key 2, cache is {1=0, 3=3}
    # lru.put(4, 1)  #  LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    # print(lru.get(2))     #  return -1 (not found)

    # # Test case 3:
    # lru = LRUCache(2)
    # lru.put(1, 0)  # cache is {1=0}
    # lru.put(2, 2)  #  cache is {1=0, 2=2}
    # print(lru.get(1))     #  return 0, cache is {2=2, 1=0}
    # lru.put(3, 3)  #  LRU key was 2, evicts key 2, cache is {1=0, 3=3}
    # print(lru.get(2))     #  returns -1 (not found)
    # lru.put(4, 4)  #  LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    # print(lru.get(1))     #  return -1 (not found)
    # print(lru.get(3))     #  return 3
    # print(lru.get(4))     #  return 4

    # Test case 2
    # lru = LRUCache(2)
    # lru.put(2, 1)  #  cache is {2=1}
    # print(lru.get(2))     #  return 1

    # Test case 1
    # lru = LRUCache(2)
    # lru.put(1, 1)  # cache is {1=1}
    # lru.put(2, 2)  #  cache is {1=1, 2=2}
    # print(lru.get(1))     #  return 1
    # lru.put(3, 3)  #  LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    # print(lru.get(2))     #  returns -1 (not found)
    # lru.put(4, 4)  #  LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    # print(lru.get(1))     #  return -1 (not found)
    # print(lru.get(3))     #  return 3
    # print(lru.get(4))     #  return 4
