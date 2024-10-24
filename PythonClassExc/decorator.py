def log_function_call(message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Calling {func.__name__} with message: {message}")
            result = func(*args, **kwargs)
            print(f"{func.__name__} completed")
            return result
        return wrapper
    return decorator

@log_function_call("Hello from decorator!")
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
