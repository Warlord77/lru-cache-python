cache = {}  
recently_used = []  
max_size = 3

def get(key):  
    if key in cache:  
        recently_used.remove(key)  
        recently_used.append(key)  
        return cache[key]  
    else:  
        return None  

def put(key, value):  
    if key in cache:  
        cache[key] = value  
        recently_used.remove(key) 
        recently_used.append(key)  
    else:  
        if len(cache) >= max_size:  
            oldest_key = recently_used.pop(0)  
            del cache[oldest_key]  
        cache[key] = value  
        recently_used.append(key)  

def remove(key):  
    if key in cache:  
        del cache[key]  
        recently_used.remove(key)  
        return True  
    return False  

def show_cache():  
    print("Cache contents:", cache)  
    print("Usage order (oldest to newest):", recently_used)  
    return cache

# Testing the updated LRU cache
if __name__ == "__main__":  
    print("\nStep 1: PUT 'Dog' -> 'Animal'")  
    put("Dog", "Animal")  
    show_cache()  

    print("\nStep 2: PUT 'CAT' -> 'Animal' (same value, different key)")  
    put("CAT", "Animal")  
    show_cache()  

    print("\nStep 3: PUT 'NOKIA' -> 'Phone'")  
    put("NOKIA", "Phone")  
    show_cache()  

    print("\nStep 4: GET 'GOAT' (should return None)")  
    print("Retrieved value:", get("GOAT"))  
    show_cache()  

    print("\nStep 5: GET 'CAT' (should be found)")  
    print("Retrieved value:", get("CAT"))  
    show_cache()  

    print("\nStep 6: REMOVE 'DOG'")  
    remove("Dog")  
    show_cache()  

    print("\nStep 7: ADD 'RAMBO' -> 'Movie'")  
    put("RAMBO", "Movie")  
    show_cache()  

    print("\nStep 8: ADD 'CROCS' -> 'Shoes' (should evict LRU item)")  
    put("CROCS", "Shoes")  
    show_cache()  
