from .cache import Cache
from collections import OrderedDict


class MRUCache(Cache):
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
            # return value for given key
            return self.cache[key][0]

    def insert(self, key: str, value: int) -> None:
        """
        Storing Key: [value, state] so that when returning state of cache we can sort that using state
        """
        state = self.STATE
        if len(self.cache) == self.capacity and self.cache.get(key) is None:
            item = self.cache.popitem(last=True)
            state = item[1][1]  # State of popped item

        # IF key is already present then update value other wise add to cache
        if self.cache.get(key) is not None:
            self.cache[key][0] = value
        else:
            self.cache[key] = [value, state]
        # If state is changed to popped element then do nothing else increase by 1
        if state == self.STATE:
            self.STATE += 1
        self.cache.move_to_end(key)

    def state_of_cache(self):
        # Get list of (key, value, state)
        items = [(key, value[0], value[1]) for key, value in self.cache.items()]
        # sort list using state
        items.sort(key=lambda x: x[2])
        # returning [(key, value)]
        return [(item[0], item[1]) for item in items]
