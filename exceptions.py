from timeit import timeit

try:
    # file = open(ds1.py)
    age = int(input("age: "))
    xfactor = 10 // age
except (ValueError, ZeroDivisionError) as ex:
    print("You did not enter a valid age!")
    print(ex)
    print(type(ex))
else:
    print("No exceptions were thrown")
# finally:
#     file.close()
print("Execution continues")
# NOTE The with clause
# try:
# NOTE HERE
#     with open("app.py") as file, open("another.txt") as target:
#         print("file transfers")
#     age = int(input("age: "))
#     xfactor = 10 // age
# except (ValueError, ZeroDivisionError) as ex:
#     print("You did not enter a valid age!")
#     print(ex)
#     print(type(ex))
# else:
#     print("No exceptions were thrown")
# print("Execution continues")

code1 = """
def calc_xfactor(age):
    if age <= 0:
        raise ValueError("Age can not be zero or less")
    return 10 // age


try:
    calc_xfactor(-1)
except ValueError as error:
    pass
"""
# print(error)
print("first code= ", timeit(code1, number=10000))

code2 = """
def calc_xfactor(age):
    if age <= 0:
       return None
    return 10 // age


x_fact = calc_xfactor(-1)
if x_fact == None:
    pass
"""
# print(error)
print("second code= ", timeit(code2, number=10000))
