from app.lru_cache import LRUCache
from app.mru_cache import MRUCache
if __name__ == '__main__':
    lru = LRUCache(5)
    items = ['A', 'B', 'C', 'D', 'E', 'F', 'B', 'G']
    mru = MRUCache(5)

    for index, value in enumerate(items):
        # print(value, index)
        lru.insert(value, index)
        print(lru.state_of_cache())

    items = ['A', 'B', 'C', 'D', 'E', 'F', 'C', 'G', 'B']
    for index, value in enumerate(items):
        # print(value, index)
        mru.insert(value, index)
        print(mru.state_of_cache())
    # print(mru.get('A'))
    # print(lru.get('G'))
