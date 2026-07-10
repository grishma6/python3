# calling a function
def name():
    print("Hello")
    print("Hello Grishma")


name()

# Arguments

# first_name ->> parameter


def name(first_name, last_name):
    print(f"Hello {first_name} {last_name}")


# argument
name("grishma", "golla")


# Types of functions
def greet(name):
    print(f"Hi {name}")


print(greet("Grishma"))

# Keyword Arguments


def increment(number, by):
    return number + by


print(increment(number=2, by=3))

# Default Arguments
# optional parameters should come after required parameters


def increement(number, by=1):
    return number + by


print(increement(5))

# xargs


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))
