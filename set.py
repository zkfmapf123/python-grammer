# SET

a = {
    1,2,2,2,3,3,3,4,4,4,5
}

print(a, type(a))

b = { 
    2,3,3,6,7
}

## 여집합
print(a-b)
print(b-a)

## 합집합
print(a | b)

## 교집합
print(a & b)

## A 차집합 + B 차집합
print(a ^ b)

## Method
s = [1,2,2,2,2,2,3,3,3,3,3,4,5]
print(s)

### Convert
setA = set(s)
print(setA)

setA.add(10)
print(setA)

setA.remove(1)
print(setA)

setA.clear()
print(setA)

## Example

my_friends = ["a","b","c","d"]
you_frineds = ["b","c","f","z","i"]

print(set(my_friends) & set(you_frineds)) ## 교집합
print(set(my_friends + you_frineds)) ## 합집합
