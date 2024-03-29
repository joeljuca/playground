# See: https://learnxinyminutes.com/docs/python/


def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")


greet("World")  # => Hello, World!
greet("Joel")  # => Hello, Joel!
greet("Joel", "Welcome")  # => Welcome, Joel!
