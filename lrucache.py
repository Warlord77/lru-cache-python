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
            least_used_key = min(frequency, key=frequency.get)
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
    return cache
