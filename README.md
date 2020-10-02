# Cache Eviction Policy
Design CacheEvictionPolicy with 2 strategy LRU(Least recently used), MRU(Most recent used)
Notes:
- Cache size = 5
- Methods exposed to user:
○ Insert(key, value) - consider key, value as integer
○ Get(key) returns value
○ StateOfCache() return [{key, value}]

Example: LRU
Input: A B C D E F B G
1. A
2. A B
3. A B C
4. A B C D
5. A B C D E
6. F B C D E
7. F B C D E
8. F B G D E

Example: MRU
Input: A B C D E F C G B
1. A
2. A B
3. A B C
4. A B C D
5. A B C D E
6. A B C D F
7. A B C D F
8. A B G D F
9. A B G D F

## App Requirements
- Python3 should be installed

## To run the application
```
python3 main.py
```

### This will produce results for the given input- 
```
For LRU
[('A', 0)]
[('A', 0), ('B', 1)]
[('A', 0), ('B', 1), ('C', 2)]
[('A', 0), ('B', 1), ('C', 2), ('D', 3)]
[('A', 0), ('B', 1), ('C', 2), ('D', 3), ('E', 4)]
[('F', 5), ('B', 1), ('C', 2), ('D', 3), ('E', 4)]
[('F', 5), ('B', 6), ('C', 2), ('D', 3), ('E', 4)]
[('F', 5), ('B', 6), ('G', 7), ('D', 3), ('E', 4)]

```
```
For MRU
[('A', 0)]
[('A', 0), ('B', 1)]
[('A', 0), ('B', 1), ('C', 2)]
[('A', 0), ('B', 1), ('C', 2), ('D', 3)]
[('A', 0), ('B', 1), ('C', 2), ('D', 3), ('E', 4)]
[('A', 0), ('B', 1), ('C', 2), ('D', 3), ('F', 5)]
[('A', 0), ('B', 1), ('C', 6), ('D', 3), ('F', 5)]
[('A', 0), ('B', 1), ('G', 7), ('D', 3), ('F', 5)]
[('A', 0), ('B', 8), ('G', 7), ('D', 3), ('F', 5)]
```

### To test more:
- Go to main.py
```
lru = LRUCache(size_of_cache)
then use CacheInterface

same with MRU cache
```