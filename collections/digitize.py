def digitize(num):
    return list(map(int, str(num)))

if __name__ == "__main__":
    print(digitize(321))
    print(digitize(900))
    print(digitize("xyz"))