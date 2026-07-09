import math

print("grishma")
print('*'*10)

# Strings
course = "python programming"
print(len(course))
print(course[-1])
print(course[0:3])
print(course[0:])
print(course[:])

# escape sequences
# \'
# \"
# \\
# \n

course = "python \"programming"
print(course)

# Formatting strings
first = "Grishma"
last = "Golla"
full = f"{first} {last}"  # concatenation first + last
print(full)

# String Functions/Methods
course = "python programming"
print(course.upper())
print(course.lower())
print(course.strip())
print(course.lstrip())
print(course.rstrip())
print(course.find("Pro"))
print(course.title())
print(course.replace("p", "j"))
print("pro" in course)
print("swift" not in course)


# Numbers
print(5 + 2)
print(5 - 2)
print(5 * 2)
print(5 / 2)
print(5 // 2)  # for integer value
print(5 % 2)
print(5 ** 2)
print(abs(-2.9))
print(math.ceil(2.9))
print(round(2.9))
