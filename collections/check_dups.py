def check_duplicates(lst):
    return len(lst) != len(set(lst))


if __name__ == "__main__":
    lst1 = [1,2,3,3,5]
    lst2 = [1,2,3]
    print(check_duplicates(lst1))
    print(check_duplicates(lst2))