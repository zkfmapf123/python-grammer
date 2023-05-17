## Dict Contsutctor 1
d = {
    "x" : 10,
    "y" : 20
}
print(d)

d['XX'] = 123123
print(d)
d[1] = 110123   
print(d)

## Dict Constructor 2
print(dict(a = 10, b= 20))


## Method
d = {
    "x" : 10,
    "y" : 20
}

# help(d)

print(d.keys())
print(d.values())

x = {"a" : 10, "b" : 20}
y = {"a" : 100, "b" : 200}
print(x, y)
x.update(y) ## Overriding

print(x, y)

x = {"a" : 100, "b" : 200, "c" : 300}
y = {"d" : 400 , "e" :500}
x.update(y)
print(x) ## x = [...x, ...y]

print(x.get("a"), x.get("aa"), type(x.get('aa')))

x.pop("a")
print(x)

x.clear()
print(x)

a = {"a" : 100, "b" : 200}
print('a' in a)
print('c' in a)

## dict copy 

### Shallow copy
x = {"a" : 1}
y = x

x["a"] = 100
print(x,y)

### Deep Copy
x = {"a" : 1}
y = x.copy()

x["a"] = 100
print(x,y)

## Example
fruits = {
    "apple" : 1000,
    "banana" : 5000,
    "orange" : 3000
}

print(fruits["apple"])
print(fruits["orange"])
print(fruits["1234"]) ## Error
