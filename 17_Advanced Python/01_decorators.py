def decorator(func):
    def wrapper():
        print("i am about to execute a function...")
        func()
        print("i have executed this function..")
    return wrapper

@decorator
def say_hello():

    print("hello!")

say_hello()


# f = decorator(say_hello)
# f()