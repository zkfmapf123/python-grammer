x = 0

if x < 0:
    print("nagative")
elif x == 0:
    print("x : ", x)
else:
    print("positive")

## 띄어쓰기 주의
a,b = 5,10
if a > 0:
    print("a is positive")
    if b > 0:
        print("b is positive")

print(a == b)
print(a != b)
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)
print(a >0 and b> 0) # a > 0 && b > 0 이거는 안됌
print(a >0 or b > 0) # a > 0 || b > 0 이거는 안됌

y = [1,2,3]
x = 1

if x in y:
    print("x in y")

if 4 in y:
    print("4 in y")

a,b = 1,2

if a == b:
    print("Equal")

if not a == b:
    print("Not Equal")

if a!=b:
    print("Not Equal")

## Example
is_ok = True
if is_ok:
    print("OK!")

is_ok = 1
if is_ok:
    print("OK!")
else:
    print("No")

str1 = "str" ## Exists
if str1: 
    print("exists")

str2 = [] ## Not Exists
if str2:
    print("exits")
else:
    print("not exitss")

