class Animal:
    def __init__(self, species):
        self.species = species
        
if __name__ == '__main__':
    string = 'Hello, world'
    
    print(isinstance(string, str))
    print(isinstance(string, (int, str)))
    
    cat = Animal('cat')
    print(isinstance(cat, Animal))