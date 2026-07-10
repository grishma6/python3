# for
for number in range(1, 4):
    print("Grishma", number, (number + 1) * ".")


# for else
successful = True
for number in range(3):
    # if this is true this block is executed
    print("attempt")
    if successful:
        print("Successful")
        break
    # else this is executed
else:
    print("Attempt not successful")

# Nested Loops
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

# Iterables
print(type(5))
print(type(range(5)))

for x in [1, 2, 3, 4, 5]:
    print(x)

# while loops
number = 1000
while number > 0:
    print(number)
    number //= 2

command = ""
while command != "quit" and command == "QUIT":
    command = input(">")
    print("ECHO", command)

# Infinite Loops
while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break
