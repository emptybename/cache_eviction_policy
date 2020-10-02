from .cache import Cache

from collections import OrderedDict


class LRUCache(Cache):
    STATE = 0

    def __init__(self, capacity):
        super().__init__(capacity)
        self.cache = OrderedDict()

    def overflow(self):
        return len(self.cache) > self.capacity

    def get(self, key: str) -> int:
        if self.cache.get(key) is None:
            return -1
        else:
            self.cache.move_to_end(key)
            # Return value for given key
            return self.cache[key][0]

    def insert(self, key: str, value: int) -> None:
        """
        Storing Key: [value, state] so that when returning state of cache we can sort that using state
        """
        state = self.STATE
        if self.cache.get(key) is None and len(self.cache) == self.capacity:
            item = self.cache.popitem(last=False)
            state = item[1][1]  # state of popped item
        if self.cache.get(key):
            self.cache[key][0] = value
        else:
            """ Inserting new element in cache """
            self.cache[key] = [value, state]
        self.cache.move_to_end(key)
        if state == self.STATE:
            self.STATE += 1

    def state_of_cache(self):
        # Get list of (key, value, state)
        items = [(key, value[0], value[1]) for key, value in self.cache.items()]
        # sort list using state
        items.sort(key=lambda x: x[2])
        # returning [(key, value)]
        return [(item[0], item[1]) for item in items]
