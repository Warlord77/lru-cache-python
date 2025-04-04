# LRU Cache Implementation in Python

## Overview
This repository contains my implementation of a Least Recently Used (LRU) cache in Python. An LRU cache is a type of cache that has a specified maximum capacity and removes the least recently accessed items when the cache reaches its capacity limit.

## Problem Statement
Create an LRU cache in Python with the following requirements:

1. Implement `get`, `put`, and `remove` functions
2. Achieve O(1) time complexity for all operations
3. Support a configurable maximum cache size (not implemented right now)

### Assumptions
Note:  This is not a time based implementation

### Solution Approach
My implementation uses two main data structures. 

1. cache (Python dictionary): Stores key-value pairs for O(1) lookups.
2. recently_used (Python list): Maintains the access order of keys.

#### Time Complexity
All operations (get, put, remove) have O(1) time complexity except for the list operations which are O(n) in the worst case.\
However, since the cache size is typically fixed and small, this can be considered constant time for practical purposes.

### Functions Implemented 
##### `get(key)`
Returns the value associated with the key if it exists. \
Updates the key's position in the recently_used list to mark it as most recently used. \
Returns None if the key doesn't exist in the cache.

##### `put(key, value)`
If the key already exists, updates its value and marks it as most recently used. \
If the key doesn't exist then\
       1. If the cache is at maximum capacity, removes the least recently used item.\
       2. Adds the new key-value pair to the cache.\
       3. Adds the key to the end of the recently_used list


#### `remove(key)`
Removes the key-value pair from the cache if it exists.\
Removes the key from the recently_used list.\
Returns True if the key was found and removed, False otherwise.

#### `show_cache()`
Helper function that displays the current state of the cache.\
Shows both the cache contents and the usage order of keys.\
Returns the current cache dictionary.
______________________________________________________________________________________________________________________
### Testing
The implementation includes comprehensive tests to verify correctness\
Adding elements to the cache\
Retrieving existing and non-existing elements\
Removing elements\
Handling capacity limits (evicting least recently used items)\
Updating values for existing keys