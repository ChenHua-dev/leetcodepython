from exercise.LinkedList.LC146LRUCache import LRUCache
import unittest


class TestLRUCache(unittest.TestCase):
    def test_case_1(self):
        # Test case 1
        lru = LRUCache(2)
        lru.put(1, 1)  # cache is {1=1}
        lru.put(2, 2)  #  cache is {1=1, 2=2}
        self.assertEqual(lru.get(1), 1)      #  return 1
        lru.put(3, 3)  #  LRU key was 2, evicts key 2, cache is {1=1, 3=3}
        self.assertEqual(lru.get(2), -1)     #  returns -1 (not found)
        lru.put(4, 4)  #  LRU key was 1, evicts key 1, cache is {4=4, 3=3}
        self.assertEqual(lru.get(1), -1)     #  return -1 (not found)
        self.assertEqual(lru.get(3), 3)     #  return 3
        self.assertEqual(lru.get(4), 4)     #  return 4

    def test_case_2(self):
        # Test case 2
        lru = LRUCache(2)
        lru.put(2, 1)  #  cache is {2=1}
        self.assertEqual(lru.get(2), 1)     #  return 1

    def test_case_3(self):
        # # Test case 3:
        lru = LRUCache(2)
        lru.put(1, 0)  # cache is {1=0}
        lru.put(2, 2)  #  cache is {1=0, 2=2}
        self.assertEqual(lru.get(1), 0)     #  return 0, cache is {2=2, 1=0}
        lru.put(3, 3)  #  LRU key was 2, evicts key 2, cache is {1=0, 3=3}
        self.assertEqual(lru.get(2), -1)     #  returns -1 (not found)
        lru.put(4, 4)  #  LRU key was 1, evicts key 1, cache is {4=4, 3=3}
        self.assertEqual(lru.get(1), -1)     #  return -1 (not found)
        self.assertEqual(lru.get(3), 3)     #  return 3
        self.assertEqual(lru.get(4), 4)     #  return 4

    def test_case_4(self):
        # # Test case 4:
        lru = LRUCache(2)
        lru.put(2, 1)  # cache {2=1}
        lru.put(2, 2)  #  cache {2=2} b/c need to update the value for the key
        self.assertEqual(lru.get(2), 2)     #  return 2, cache is {2=1}
        lru.put(1, 1)  #  LRU key was 2, evicts key 2, cache is {1=0, 3=3}
        lru.put(4, 1)  #  LRU key was 1, evicts key 1, cache is {4=4, 3=3}
        self.assertEqual(lru.get(2), -1)     #  return -1 (not found)

    def test_case_5(self):
        # Test case 5
        lru = LRUCache(2)
        self.assertEqual(lru.get(2), -1)     #  return -1
        lru.put(2, 6)  # cache is {2=6}
        self.assertEqual(lru.get(1), -1)     #  return -1
        lru.put(1, 5)  #  LRU key was 2, evicts key 2, cache is {2=6, 1=5}
        lru.put(1, 2)  #  LRU key was 2, evicts key 2, cache is {2=6, 1=2}
        self.assertEqual(lru.get(1), 2)     #  returns 2 (not found)
        self.assertEqual(lru.get(2), 6)     #  returns 6 (not found)

