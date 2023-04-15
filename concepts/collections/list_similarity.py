def similarity(x,y):
    return [item for item in x if item in y]

if __name__ == "__main__":
    x = [1,2,3,4,5]
    y = [1,2,3]
    
    print(similarity(x,y))