import math


def fizz_buzz(input):
    if input % 3 == 0 and input % 5 != 0:
        m = "fizz"
    elif input % 5 == 0 and input % 3 != 0:
        m = "buzz"
    elif input % 5 == 0 and input % 3 == 0:
        m = "fizz buzz"
    else:
        m = input
    return m


def save_user(**user):
    print(user)
    print(user["name"])


def greet(name_one, name_two):
    print(f"Welcome aboard {name_one} {name_two}")


def get_greet(name_one, name_two=""):
    return f"Hello {name_one} {name_two}"


def multiply(*nums):
    total = 1
    for num1 in nums:
        total *= num1
    return total


print("Hello world")
print("*" * 10)
x = 8
print(x)
is_published = False
name = "  Program ming"
print(len(name))
print(name[-1])
print(name[0:5])
# \"
# \'
# \n
first_name = "Python"
full = f"{first_name} {name} {len(name)} {2 * 3}"
print(full)
print(name.lower())
print(name.upper())
print(name.strip())
print(name.title())
print(name.find("ming"))
print(name.replace("min", "Min"))
print("min" not in name)
print(10 + 3)
print(10 - 3)
print(10 // 3)
print(10 / 3)
print(10 ** 3)
print(10 * 3)
print(10 % 3)
#x += 2
print(round(2.2))
print(abs(-2.2))
print(math.floor(2.2))
# math module on google
x = input("x: ")
print(type(x))
y = int(x) + 1
print(f"x: {x}, y: {y}")
# FALSY 0 "" None
temperature = 15
if temperature > 30:
    print("Warm")
elif temperature > 20:
    print("Nice")
else:
    print("Cold")
print("Done")
age = 12
message = "elgible" if age >= 18 else "not"
print(message)
high_income = False
credit = True
student = False
if (high_income or credit) and not student:
    print("eligible")
else:
    print("not")
# short circuit evaluation it reads from left to right in AND case if first false it doesnt check the rest
my_age = 22
if 18 <= my_age < 65:
    print("Adult")

for number in range(1, 10, 2):
    print("attempt", number, number * ".")

successful = False
for num in range(3):
    print("attempt")
    if successful:
        print("successful")
        break
else:
    print("attempted 3 times but failed")

for x1 in range(3):
    for y1 in range(4):
        print(f"({x1},{y1})")
print(type(range(5)))
# 11 th video continued
for x in "Python":
    # for x in [1,2,3,4]:

    print(x)

n2 = 100
while n2 > 0:
    print(n2)
    n2 //= 2
command = ""
while command.lower() != "quit":  # or command != "QUIT":
    command = input()
    print("ECHO", command)

count = 0

for loop in range(1, 10):
    if (loop % 2 == 0):
        print(loop)
        count += 1
print(f"We have {count} even numbers")

greet("aaryaman", "saini")
greet("rakesh", "saini")
m1 = get_greet("neetu", "saini")
print(m1)
print(get_greet("a", name_two="b"))  # name_two is a keyword argument
print(multiply(2, 3, 4, 5))
save_user(id=1, name="John", age=22)

print(fizz_buzz(11))
