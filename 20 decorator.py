# decorator - a function within a function

def my_decorator(target_function):
    def wrapper_function():
        return "I love " + target_function() + " language"
    return wrapper_function

@my_decorator
def target_function():
    return "Python"

target_function()



