def merge_two_dicts(x,y):
    z = x.copy()
    z.update(y)
    return z

if __name__ == "__main__":
    x = {"A": 1, "B": 2}
    y = {"C": 3, "D": 4}
    
    z = merge_two_dicts(x,y)
    