from .interfaces.cache_interface import CacheInterface
from typing import List


class Cache(CacheInterface):

    def __init__(self, capacity: int):
        self.capacity = capacity

    def insert(self, key: str, value: int) -> None: pass

    def get(self, key: str) -> int: pass

    def state_of_cache(self): pass
