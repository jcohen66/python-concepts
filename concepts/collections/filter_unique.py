def filter_unique(data):
    return list(set(data))

if __name__ == "__main__":
    lst = [1,2,3,2,5,6,6,5,7]
    print(filter_unique(lst))
    print(filter_unique("cat"))
    print(filter_unique("cattle"))
    