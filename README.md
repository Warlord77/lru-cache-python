# Frequency-Based Cache Implementation

A simple Python cache implementation that uses a frequency-based eviction policy. This implementation tracks how often each key is accessed and removes the least frequently used item when the cache reaches its capacity.

## Features

- Fixed-size cache with configurable maximum capacity
- Frequency-based eviction policy (LFU - Least Frequently Used)
- Basic cache operations: get, put, and remove
- Cache visualization functionality

## Usage

```python
# Initialize the cache (already done in the implementation)
# Default max_size is 5
cache = {}
frequency = {}
max_size = 5

# Add items to the cache
put("key1", "value1")
put("key2", "value2")

# Retrieve items
value = get("key1")  # Returns "value1" and increases access frequency

# Remove items
removed = remove("key1")  # Returns True if successful

# Display cache contents and access frequencies
show_cache()
```

## API Reference

### `get(key)`

Retrieves a value from the cache by its key.

- If the key exists, increments its access frequency and returns the associated value
- If the key doesn't exist, returns `None`

### `put(key, value)`

Adds or updates a key-value pair in the cache.

- If the key already exists, updates its value and increments its access frequency
- If the key doesn't exist and the cache is full, removes the least frequently used item before adding the new one
- If the key doesn't exist and the cache has space, adds the new key-value pair with an initial frequency of 1

### `remove(key)`

Removes a key-value pair from the cache.

- If the key exists, removes it from both the cache and frequency dictionaries and returns `True`
- If the key doesn't exist, returns `False`

### `show_cache()`

Displays the current contents of the cache and the access frequency for each key.
Returns the current cache dictionary.

## Time Complexity

| Operation | Average Case | Worst Case | Notes |
|-----------|--------------|------------|-------|
| `get(key)` | O(1) | O(1) | Dictionary lookup and increment operations are constant time |
| `put(key, value)` | O(1) | O(n) | When cache is full, finding the least frequent item takes O(n) time where n is the current cache size |
| `remove(key)` | O(1) | O(1) | Dictionary deletion operations are constant time |
| `show_cache()` | O(1) | O(1) | Printing dictionaries is constant time |

The most expensive operation is the eviction policy in the `put()` method when the cache is full. The implementation uses `min(frequency, key=frequency.get)` which requires iterating through all keys in the frequency dictionary to find the one with the minimum value, resulting in O(n) time complexity.


## Example

```python
# Add some items
put("A", 1)
put("B", 2)
put("C", 3)

# Access some items multiple times
get("A")
get("A")
get("B")

# Show the cache state
show_cache()
# Output:
# Cache contents: {'A': 1, 'B': 2, 'C': 3}
# Access frequency: {'A': 3, 'B': 2, 'C': 1}

# Add more items to trigger eviction
put("D", 4)
put("E", 5)
put("F", 6)  # This will evict 'C' since it has the lowest frequency

# Show the cache state again
show_cache()
# Output:
# Cache contents: {'A': 1, 'B': 2, 'D': 4, 'E': 5, 'F': 6}
# Access frequency: {'A': 3, 'B': 2, 'D': 1, 'E': 1, 'F': 1}
```

## Test-Cases-Output
```
Test: LRU Cache in Action

Initial cache and frequency:
Cache contents: {'A': 'Value 1', 'B': 'Value 2', 'D': 'Value 4', 'E': 'Value 5', 'F': 'Value 6'}
Access frequency: {'A': 1, 'B': 1, 'D': 1, 'E': 1, 'F': 1}

Accessing A:
Cache contents: {'A': 'Value 1', 'B': 'Value 2', 'D': 'Value 4', 'E': 'Value 5', 'F': 'Value 6'}
Access frequency: {'A': 2, 'B': 1, 'D': 1, 'E': 1, 'F': 1}

Accessing B:
Cache contents: {'A': 'Value 1', 'B': 'Value 2', 'D': 'Value 4', 'E': 'Value 5', 'F': 'Value 6'}
Access frequency: {'A': 2, 'B': 2, 'D': 1, 'E': 1, 'F': 1}

Accessing D:
Cache contents: {'A': 'Value 1', 'B': 'Value 2', 'D': 'Value 4', 'E': 'Value 5', 'F': 'Value 6'}
Access frequency: {'A': 2, 'B': 2, 'D': 2, 'E': 1, 'F': 1}

Accessing E:
Cache contents: {'A': 'Value 1', 'B': 'Value 2', 'D': 'Value 4', 'E': 'Value 5', 'F': 'Value 6'}
Access frequency: {'A': 2, 'B': 2, 'D': 2, 'E': 2, 'F': 1}

Accessing F:
Cache contents: {'A': 'Value 1', 'B': 'Value 2', 'D': 'Value 4', 'E': 'Value 5', 'F': 'Value 6'}
Access frequency: {'A': 2, 'B': 2, 'D': 2, 'E': 2, 'F': 2}

Adding a new item G to the cache:
Evicting A with frequency 2
Cache contents: {'B': 'Value 2', 'D': 'Value 4', 'E': 'Value 5', 'F': 'Value 6', 'G': 'Value G'}
Access frequency: {'B': 2, 'D': 2, 'E': 2, 'F': 2, 'G': 1}

Removing item B from the cache:
Cache contents: {'D': 'Value 4', 'E': 'Value 5', 'F': 'Value 6', 'G': 'Value G'}
Access frequency: {'D': 2, 'E': 2, 'F': 2, 'G': 1}

Accessing D:
Cache contents: {'D': 'Value 4', 'E': 'Value 5', 'F': 'Value 6', 'G': 'Value G'}
Access frequency: {'D': 3, 'E': 2, 'F': 2, 'G': 1}

Accessing E:
Cache contents: {'D': 'Value 4', 'E': 'Value 5', 'F': 'Value 6', 'G': 'Value G'}
Access frequency: {'D': 3, 'E': 3, 'F': 2, 'G': 1}

Accessing A:
Cache contents: {'D': 'Value 4', 'E': 'Value 5', 'F': 'Value 6', 'G': 'Value G'}
Access frequency: {'D': 3, 'E': 3, 'F': 2, 'G': 1}

Accessing B:
Cache contents: {'D': 'Value 4', 'E': 'Value 5', 'F': 'Value 6', 'G': 'Value G'}
Access frequency: {'D': 3, 'E': 3, 'F': 2, 'G': 1}

Accessing F:
Cache contents: {'D': 'Value 4', 'E': 'Value 5', 'F': 'Value 6', 'G': 'Value G'}
Access frequency: {'D': 3, 'E': 3, 'F': 3, 'G': 1}

Adding a new item H to the cache:
Cache contents: {'D': 'Value 4', 'E': 'Value 5', 'F': 'Value 6', 'G': 'Value G', 'H': 'Value H'}
Access frequency: {'D': 3, 'E': 3, 'F': 3, 'G': 1, 'H': 1}
```