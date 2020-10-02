from abc import ABC, abstractmethod
from typing import List


class CacheInterface(ABC):
    @abstractmethod
    def insert(self, key: str, value: int) -> None: pass

    @abstractmethod
    def get(self, key: str) -> int: pass

    @abstractmethod
    def state_of_cache(self): pass
