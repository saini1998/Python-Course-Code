from collections import deque
from array import array
from sys import getsizeof


letters = ["a", "b", "c"]
for index, letter in enumerate(letters):
    print(index, letter)

# Add
letters.append("d")
letters.insert(0, "-")
print(letters)
# Remove
letters.pop()
letters.pop(0)
print(letters)
print(letters.count("b"))
if "a" in letters:
    print(letters.index("a"))
matrix = [[0, 1], [2, 3]]
letters[0] = "A"
print(letters[::2])
zeros = [0] * 5
combined = zeros + letters
numbers = list(range(20))
print(numbers[::-2])
chars = list("hi there")
print(matrix)
print(zeros)
print(combined)
print(numbers, chars)

numlist = [1, 2, 4, 4, 4, 9]
f1, *o1, l1 = numlist
print(f1, l1)
print(o1)

sample_letters = ["a", "b", "c", "d"]
sample_letters.remove("b")
print(sample_letters)
del sample_letters[0:2]
print(sample_letters)
sample_letters.clear()
print(sample_letters)
num1 = [2, 6, 4, 10, 1, 7]
num1.sort()
print(num1)
print(sorted(num1, reverse=True))
print(num1)

item_list = [("p1", 10), ("p2", 9), ("p3", 12)]


# def sort_item(item1):
#     return item1[1]


item_list.sort(key=lambda item1: item1[1])
print(item_list)
# prices = list(map(lambda item: item[1], item_list))
prices = [item[1] for item in item_list]  # comprehension
print(prices)
# x = list(filter(lambda item: item[1] >= 10, item_list))
filtered = [item for item in item_list if item[1] >= 10]
print(filtered)

lis1 = [1, 2, 3]
lis2 = [10, 20, 30]
print(list(zip("abc", lis1, lis2)))

# Stacks
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last = browsing_session.pop()
print(last)
print(browsing_session)
if browsing_session:
    print("redirect", browsing_session[-1])
# if not browsing_session:
#     browsing_session[-1]

# Queues
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
if not queue:
    print("empty")
# Tuples
# point = ()
# point = 1,2
# point = (1,2) + (3,4)
# point = (1,2) * 3
point = tuple("hello world")
print(point)
point1 = (1, 2, 3)
x, y, z = point1
print(x, y, z)
# tuple object does not support item assignment
a1 = 10
b1 = 11
a1, b1 = b1, a1  # swapping variables
a2, b2 = 3, 4
print(a1, b1, a2, b2)
# arrays
# use methods as list but these are of type so can only take those value
numz = array("i", [1, 2, 3])
# SETs

numzz = [1, 2, 2, 3, 4, 4, 2]
uniques = set(numzz)
second = {5, 6, 1, 2}
print(uniques, second)
# set object does not support indexing
print(uniques | second)
print(uniques & second)
print(uniques - second)
print(uniques ^ second)
if 1 in uniques:
    print("yes")

# Dictionaries
d = {"x": 1, "y": 2}
d1 = dict(x=1, y=2)
d1["x"] = 10
d1["z"] = 30
print(d1.get("A", 0))
del d1["x"]
print(d1)
for key, values in d1.items():
    print(key, values)
# We can use comprehension with lists, sets, dictionaries
vals = {x: x*2 for x in range(5)}
print(vals)

# Generator expressions
# from sys import getsizeof
tups = (x * 2 for x in range(100000))
print(getsizeof(tups))
# NOTE object of type 'generator' has no len()

# unpacking operator
num2 = [1, 2, 3]
print(*num2)
num2 = [*range(5), *"hello"]
fir1 = [1, 2]
sec1 = [3]
num3 = [*fir1, *sec1]
print(num2)
print(num3)
com1 = dict(x=1)
com2 = dict(x=10, y=20)  # this x gets taken
com3 = {**com1, **com2, "z": 30}
print(com3)
