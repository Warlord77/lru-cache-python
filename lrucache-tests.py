from lrucache import get , put , remove, show_cache

def test_lru_cache():
    global cache, recently_used, max_size
    cache = {}  
    recently_used = []  
    max_size = 3  

    print("TEST 1: Adding elements")
    put("Dog", "Animal")
    put("Cat", "Animal")
    put("Nokia", "Phone")
    cache = show_cache()
    assert cache == {'Dog': 'Animal', 'Cat': 'Animal', 'Nokia': 'Phone'}
    
    print("\nTEST 2: Retrieving elements")
    assert get("Dog") == "Animal"  
    assert get("Goat") is None  
    show_cache()

    print("\nTEST 3: Deleting elements")
    assert remove("Dog") is True  
    assert remove("Goat") is False  
    show_cache()

    print("\nTEST 4: Same name, different value")
    put("Dog", "Pet")  
    put("Phone1", "Samsung")
    put("Phone2", "Samsung") 
    show_cache()
    #assert cache == {"Dog": "Pet", "Phone1": "Samsung", "Phone2": "Samsung"}

    print("\nAll tests passed successfully!")



test_lru_cache()
