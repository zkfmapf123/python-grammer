some_list = [10,20,30,40,50]

## use while
i = 0
while i < len(some_list):
    print(">> ", some_list[i])
    i+=1

## use for
for i in some_list:
    print(i)

for s in "abcde":
    print(s)

for word in ["my", "name","is","leedonggyu"]:
    print(word)

## for else (finally)
for fruit in ("apple", "banana","orange"):
    print(fruit)
else:
    print("all eat")

## use Range
num_list = [0,1,2,3,4,5,6,7,8,9]
for i in num_list:
    print("use for >> ", i)

for i in range(10):
    print("use range >> ", i)

for i in range(2,10):
    print("use range >>" , i)

## enumerate
i :int = 0
for fruit in ["apple", "banana", "orange"]:
    print("use for fruit >> ",i, fruit)
    i+=1

for i,furit in enumerate(["apple", "banana", "orange"]):
    print("use enumerate fruit >> ",i, fruit)

## Zip
days = ("Mon", "Tue","Wed")
fruites = ("apple", "banana", "orange")
drinks = ["coffee", "tea", "bear"]

## Required 월요일(아침+커피) -> 화요일(바나나+티) ...
## use For
for i, day in enumerate(days):
    print(day," >> ", fruites[i], " + ", drinks[i])

## use zip
for day, fruit, drink in zip(days, fruites, drinks):
    print(day," >> ", fruit, " + ", drink)

## Dict use For
d = {}
d["x"] = 100
d["y"] = 200

## print only key
for k in d:
    print(k)

for k,v in d.items():
    print(k," >> ",v)

print(d.items())
