from datetime import date, timedelta

class DataInterval:
    BEGINNING_OF_TIME = date(1,1,1)
    END_OF_TIME = date(5_000,1,1)
    
    def __init__(self, start, end):
        if start is None:
            start = self.BEGINNING_OF_TIME
        if end is None:
            end = self.END_OF_TIME
        assert start <= end, (start, end)
        self.start = start
        self.end = end
        
    @classmethod
    def all(cls):
        return cls(cls.BEGINNING_OF_TIME, cls.END_OF_TIME)
    
    
