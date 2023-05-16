import math

num: int = 29
name: str = "leedonggyu"
isMan: bool = True

print(num, type(num))
print(name, type(name))
print(isMan, type(isMan))

# 1. overwrite
num: str = name
print(num, type(num)) ## leedonggyu (string)

# 2. casting
new_num: int = int('1111')
print(new_num, type(new_num)) ## 1111 (int)

# 3. print
print("Hi")
print("Hello", "leedonggyu")
print("Hi", "Mike","123123", sep="...", end="\n")
print("Hi", "Mike","123123", sep="...", end="\n")
print("Hi", "Mike","123123", sep="...", end="endend\n")

# 4. Math
print(2 + 2)
print(5 - 2)
pie : int = 3.141414
print(pie)
print(round(pie,2))

r = math.sqrt(25)
print(r)

y = math.log2(10)
print(y)

# 5. string
print("test")
print('say I dont\'t know')
print("say \"I don't know\"")
print(r'c:\name\name')

## 6. Multiline
print("""
    line1
    line2
    line3
""")

print('Hi ' * 3 + 'Mike.')
print('Py' + 'thon')
prefix : str = "Py"
s = ('aaaaa' + prefix)
## s = ("a" * 5 + prefix)
print(s)

## 7. Index, Slice
word: str = "python"
print(word[0])
print(word[1])
print(word[-1])
print(word[0:3]) ## pyt
print(word[2:3]) ## 2 <= x < Index -> t
print(word[2:4]) ## th
print(word[2:5]) ## tho
print(word[1:])

word = 'j' + word[1:]
print(word)  # jython
print(word[:]) # jython

## 8. string method
s : str = "My Name is Mike. Hi Mike"
print(s)
print(s.startswith("My"))
print(s.startswith("MMY"))

print(s.find("Mike")) ## Start With Front
print(s.rfind("Mike")) ## Start With Back

print(s.count("Mike"))
print(s.capitalize())
print(s.lower())
print(s.title())
print(s.upper())

## 9. string overwrite
a : str = "a is {}".format("leedonggyu")
print(a)

aaa: str = "a is {0} {1} {2}".format('1','2','3')
print(aaa)

introduce: str = "My name is {0} nice to {1} you, Watashi ha {1} {0}".format("leedonggyu", "meet")
print(introduce)

introduceUseVars: str = "My name is {name} {family} ha {family} {name}".format(name="jun", family="donggyu")
print(introduceUseVars)

print(1, type(int(1)), type(str(1)), bool(str))
