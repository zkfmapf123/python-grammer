# 1. use enumerate()

def use_enumerate_bad_code(animals=["dog", "cat", "moose"]) -> None:
    """
        None
    """
    for i in range(len(animals)):
        print(animals[i])


def use_enumerate_good_code(animals=["dog", "cat", "moose"]) -> None:
    """
        None
    """
    for i, animal in enumerate(animals):
        print(i, animal)

# 2. FileIo 및 open, close문은 with를 사용하라


def read_file_bad_code(file_name: str) -> None:
    """
        None
    """
    f = open(file_name, "r+")
    str = f.read()
    print(str)
    f.close()


def read_file_good_code(file_name: str) -> None:
    """
        None
    """

    with open(file_name, "r+") as f:
        str = f.read()
        print(str)

# 3. if use None -> required "is"


my_num = 10


def use_none_bad_code(num: int):
    if num == None:
        print("None")


def use_none_good_code(num: int):
    if num is None:
        print("None")

# 4. if many backplash in string use "primitive string"


print("the file is in :C\\Users\\AI\\Desktop||Info")  # Bad Code
print(r"The file is in C:\Users\Ai\Desktop\Archive")  # Good Code

# 5. use f string

print("{} {} {}".format("a", "b", "c"))

a, b, c, = "a", "b", "c"
print(f"{a}, {b}, {c}")

# 6. shallow copy & deep copy


def get_list_shallow_copy(li: list[str]) -> list[str]:
    return li


def get_list_deep_cpy(li: list[str]) -> list[str]:
    return li.copy()


new_list = [10, 20, 30, 40, 50]

shallow_cpy_list = get_list_shallow_copy(new_list)
deep_cpy_list = get_list_deep_cpy(new_list)

new_list[0] = -10

print(shallow_cpy_list, deep_cpy_list)

# 7. Powerful Dictionary method (.get, .setdefault)

friends = {
    "leedonggyu": "devops",
    "limjeahyock":  "frontend",
    "kimboyun": "frontend"
}

if friends.get("another"):
    print("exists")
else:
    friends.setdefault("another", "nothing")

print(friends)

# map, filterin typescript

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list = [n + 100 for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
print("map >> ", list)

list = [n for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] if n % 2 == 0]
print("filter >> ", list)
