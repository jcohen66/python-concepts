class Engine:
    def __call__(self, *args, **kwargs):
        if args:
            print(args)
        
        if kwargs:
            print(kwargs)
            
        print("Running engine!")
        
def function():
    pass
        
if __name__ == '__main__':
    var = 'x'
    
    engine = Engine()
    engine('BMW', fuel='Electric')
    
    print(callable(function))
    print(callable(engine))
    
    for func in [engine,var, function]:
        if callable(func):
            func()