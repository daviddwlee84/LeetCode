from Naive460 import LFUCache as Naive

def test_Naive():
    cache = Naive(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1         # returns 1
    cache.put(3, 3)                  # evicts key 2
    assert cache.get(2) == -1        # returns -1 (not found)
    assert cache.get(3) == 3         # returns 3
    cache.put(4, 4)                  # evicts key 1
    assert cache.get(1) == -1        # returns -1 (not found)
    assert cache.get(3) == 3         # returns 3
    assert cache.get(4) == 4         # returns 4

    cache = Naive(0)
    cache.put(0, 0)
    assert cache.get(0) == -1

    cache = Naive(2)
    cache.put(2, 1)
    cache.put(3, 2)
    assert cache.get(3) == 2
    assert cache.get(2) == 1
    cache.put(4, 3)   # Because 3, 2 has same freq, use LRU => evicts key 3
    assert cache.get(2) == 1
    assert cache.get(3) == -1
    assert cache.get(4) == 3