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
