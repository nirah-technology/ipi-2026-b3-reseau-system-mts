from datetime import datetime as DateTime

def monitor_time_execution(function_to_monitor: callable):
    def wrapper(*args, **kwargs): 
        start = DateTime.now()
        result = function_to_monitor(*args, **kwargs)
        end = DateTime.now()
        print(f"Execution duration in microseconds: {(end-start).microseconds}")
        return result
    return wrapper

def trace(function_to_trace: callable):
    def wrapper(*args, **kwargs):
        print(f"Calling function {function_to_trace.__name__} with parameters args={args} and kwargs={kwargs}")
        result = function_to_trace(*args, **kwargs)
        return result
    return wrapper

@trace
@monitor_time_execution
def say_hello_word(username):
    print("Hello, world " + username)

say_hello_word(username="Nicolas")