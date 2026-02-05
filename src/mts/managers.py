from datetime import datetime as DateTime

class Chronometer:
    def __init__(self):
        self.__start: DateTime|None = None
        self.__end: DateTime|None = None

    def __enter__(self):
        print("Starting context manager for Chronometer...")
        self.__start = DateTime.now()
        return self
    
    def __exit__(self, *args, **kwargs):
        print("Exiting from context manager for Chronometer")
        self.__end = DateTime.now()

    
    def compute_delta(self) -> int:
        return (self.__end - self.__start).microseconds
    

with Chronometer() as chrono:
    print("super")
print(chrono.compute_delta())