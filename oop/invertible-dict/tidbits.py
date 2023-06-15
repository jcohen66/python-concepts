
def delete_min_key(d:dict[int,str]) -> None:
    if not d:
        return
    key = min(d)
    del d[key]

def deep_min(d):
    if isinstance(d, Mapping):
        # Values not keys.
        return min(deep_min(v) for v in d.value())
    elif isinstance(d, Iterable):
        return min(deep_min(v) for v in d)
    else:
        return d
    
class MyMapping:
    def __init__(self, d:dict[int,str]):
        d = d

# Fake mapping.        
Mapping.register(MyMapping)