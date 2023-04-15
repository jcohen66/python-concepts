def head(lst):
    # first element
    return lst[0]

def tail(lst):
    # last element
    return lst[len(lst)-1]

def initialize(end, start=0, steps=1):
    return list(range(start, end + 1, steps))

def flatten(lst):
    return [a for b in lst for a in b]

if __name__  == '__main__':
    print(initialize(5))
    print(initialize(7,1))
    print(initialize(8,1,2))
    
    print(flatten([[1,2,3], [4,5], [7,8]]))
    print(flatten([[1,2,3],[8,9]])) 

