from lrucache import get, put, remove, show_cache
cache = {}
frequency = {}
max_size = 5

def test_lfu_cache_in_action():
    print("\nTest: LFU Cache in Action")

    items = {"A": 1, "B": 2, "D": 4, "E": 5, "F": 6}
    for key, value in items.items():
        put(key, f"Value {value}")

    print("\nInitial cache and frequency:")
    show_cache()

    access_order = ['A', 'B', 'D', 'E', 'F']  
    for key in access_order:
        print(f"\nAccessing {key}:")
        get(key) 
        show_cache()  

    print("\nAdding a new item G to the cache:")
    put("G", "Value G")
    show_cache() 

    print("\nRemoving item B from the cache:")
    remove("B")
    show_cache()
    
    access_order = ['D', 'E', 'A', 'B', 'F']  
    for key in access_order:
        print(f"\nAccessing {key}:")
        get(key) 
        show_cache()  
    print("\nAdding a new item H to the cache:")
    put("H", "Value H")
    show_cache()  

if __name__ == "__main__":
    test_lfu_cache_in_action()