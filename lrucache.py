cache = {}
frequency = {}
max_size = 5

def get(key):
    if key in cache:
        frequency[key] += 1
        return cache[key]
    else:
        return None

def put(key, value):
    if key in cache:
        cache[key] = value
        frequency[key] += 1
    else:
        if len(cache) >= max_size:
            # Eviction logic: find least frequently used item
            least_used_key = min(frequency, key=frequency.get)
            print(f"Evicting {least_used_key} with frequency {frequency[least_used_key]}")
            del cache[least_used_key]
            del frequency[least_used_key]
        cache[key] = value
        frequency[key] = 1

def remove(key):
    if key in cache:
        del cache[key]
        del frequency[key]
        return True
    return False

def show_cache():
    print("Cache contents:", cache)
    print("Access frequency:", frequency)
    return list(cache.keys())  # Return only the keys for easier assertion in tests

def test_lfu_cache():
    global cache, frequency
    cache.clear()
    frequency.clear()
    
    print("TEST 1: Adding elements to cache (up to max_size)")
    put("A", "Value A")
    put("B", "Value B")
    put("C", "Value C")
    put("D", "Value D")
    put("E", "Value E")
    cache_contents = show_cache()
    assert len(cache_contents) == 5, f"Expected 5 items in cache, but got {len(cache_contents)}"
    
    print("\nTEST 2: Accessing elements to increase frequency")
    assert get("A") == "Value A"  # A frequency = 2
    assert get("A") == "Value A"  # A frequency = 3
    assert get("B") == "Value B"  # B frequency = 2
    assert get("B") == "Value B"  # B frequency = 3
    assert get("C") == "Value C"  # C frequency = 2
    assert get("Z") is None       # Non-existent key
    show_cache()

    print("\nTEST 3: Testing LFU eviction policy")
    # At this point: A=3, B=3, C=2, D=1, E=1
    # Adding F should evict either D or E (both frequency=1)
    put("F", "Value F")
    cache_contents = show_cache()
    # Check that we still have 5 items
    assert len(cache_contents) == 5, f"Expected 5 items after eviction, but got {len(cache_contents)}"
    # Check that A, B, C are still there (higher frequency)
    assert "A" in cache_contents and "B" in cache_contents and "C" in cache_contents, "Higher frequency items were incorrectly evicted"
    # Check that F was added
    assert "F" in cache_contents, "New item F was not added to cache"
    # Check that either D or E was evicted (both had frequency=1)
    assert not ("D" in cache_contents and "E" in cache_contents), "Expected either D or E to be evicted, but both remain"
    
    print("\nTEST 4: Deleting elements")
    assert remove("A") is True    # Remove existing element
    assert remove("Z") is False   # Remove non-existent element
    show_cache()
    
    print("\nTEST 5: Updating existing elements")
    put("B", "Updated B")         # Update existing value and increase frequency
    assert cache["B"] == "Updated B", "Value was not updated correctly"
    assert frequency["B"] == 4, f"Expected frequency=4 after update, got {frequency['B']}"
    show_cache()
    
    print("\nTEST 6: Testing full cache replacement")
    cache.clear()
    frequency.clear()
    
    # Fill the cache
    for i in range(1, max_size + 1):
        put(f"Item{i}", f"Value{i}")
    
    # Access some items to increase frequency
    get("Item1")  # freq = 2
    get("Item1")  # freq = 3
    get("Item2")  # freq = 2
    
    # Show current state
    show_cache()
    
    # Add more items to replace all original items with lower frequency
    for i in range(max_size + 1, max_size + 4):
        put(f"Item{i}", f"Value{i}")
        # Each new item triggers an eviction of the lowest frequency item
    
    # Show final state
    print("\nFinal cache state after multiple evictions:")
    final_cache = show_cache()
    
    # Item1 (freq=3) and Item2 (freq=2) should remain, others should be replaced
    assert "Item1" in final_cache, "Item with highest frequency was incorrectly evicted"
    assert "Item2" in final_cache, "Item with second highest frequency was incorrectly evicted"
    
    print("\nAll tests passed successfully!")

# Run the tests
if __name__ == "__main__":
    test_lfu_cache()
