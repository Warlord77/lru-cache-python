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

### Potential Optimizations

To improve the time complexity of the eviction policy:

1. **Maintain a sorted data structure**: Keep keys sorted by frequency, which would improve eviction to O(log n) but increase the complexity of updates.
2. **Use a min-heap**: Store keys in a min-heap based on frequency, which would make finding the minimum O(1) and updates O(log n).
3. **Keep a separate dictionary of frequency buckets**: Group keys by their frequency count, making it possible to find the least frequent keys in O(1) time.

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